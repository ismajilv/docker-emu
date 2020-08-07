from contextlib import contextmanager
from types import SimpleNamespace
from unittest import TestCase
from cli_interface.emu_cli import (
    start,
    stop,
    restart,
    log,
    flash,
    monitor,
    rgpio,
    ssh,
    esocket,
)
from unittest.mock import patch
from click.testing import CliRunner


class Test(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @contextmanager
    def mock_subprocess(self, popen_return_value=None, run_return_value=None):
        with patch("subprocess.Popen") as mock_popen:
            with patch("subprocess.run") as mock_run:
                with patch("time.sleep", return_value=None):
                    mock_popen.return_value = popen_return_value
                    mock_run.return_value = SimpleNamespace(
                        stdout=SimpleNamespace(
                            decode=lambda: SimpleNamespace(
                                strip=lambda: run_return_value,
                                split=lambda x: ["0.0.0.0", "0000"],
                            )
                        )
                    )

                    yield mock_popen, mock_run

    def test_emu_starts_log_success_message(self):
        # given
        with self.mock_subprocess(run_return_value=1) as (mock_popen, _):

            # when
            result = self.runner.invoke(start)

        # then
        mock_popen.assert_called_once_with(
            ["sudo", "docker-compose", "up", "--scale", "esp32=1"],
            stderr=-2,
            stdin=-1,
            stdout=-3,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Starting IoT Lab, please wait!", result.output)
        self.assertIn(
            "IoT lab started. 1 instance of ESP32 and 1 instance of Raspberry Pi are running!",
            result.output,
        )

    def test_emu_starts_log_failure_message(self):
        # given
        with self.mock_subprocess(run_return_value=None) as (mock_popen, _):

            # when
            result = self.runner.invoke(start)

        # then
        mock_popen.assert_called_once_with(
            ["sudo", "docker-compose", "up", "--scale", "esp32=1"],
            stderr=-2,
            stdin=-1,
            stdout=-3,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("IoT lab couldn't be started!", result.output)

    def test_emu_stop_logs_stop_message(self):
        # given
        any_id = 1
        with self.mock_subprocess(run_return_value=any) as (_, mock_run):

            # when
            result = self.runner.invoke(stop)

        # then
        mock_run.assert_called_with(
            ["sudo", "docker-compose", "down"], stderr=-2,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("IoT Lab stopped!", result.output)

    def test_emu_restart_logs_stop_and_start_messages(self):
        # given
        with self.mock_subprocess(run_return_value=1):

            # when
            result = self.runner.invoke(restart)

        # then
        self.assertEqual(result.exit_code, 0)
        self.assertIn(
            "IoT lab started. 1 instance of ESP32 and 1 instance of Raspberry Pi are running!",
            result.output,
        )
        self.assertIn("Starting IoT Lab, please wait!", result.output)
        self.assertIn("IoT Lab stopped!", result.output)

    def test_emu_log_success_when_called_with_esp32(self):
        # given
        given_esp32_id = 1
        with self.mock_subprocess(run_return_value=given_esp32_id) as (
            _,
            mock_run,
        ):

            # when
            result = self.runner.invoke(log, ["esp32", "--id", "1"])

        # then
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_with(["sudo", "docker", "logs", given_esp32_id])

    def test_emu_log_success_when_called_with_raspberry_pi(self):
        # given
        given_raspberry_pi_id = 1
        with self.mock_subprocess(run_return_value=given_raspberry_pi_id) as (
            _,
            mock_run,
        ):

            # when
            result = self.runner.invoke(log, ["raspberry_pi"])

        # then
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_with(["sudo", "docker", "logs", given_raspberry_pi_id])

    def test_emu_flash_success(self):
        # given
        with self.mock_subprocess(run_return_value=1) as (
            mock_popen,
            mock_run,
        ):

            # when
            result = self.runner.invoke(flash, ["--id", "1"])

        # then
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_with(
            ["idf.py", "flash", "-p", "socket://localhost:0000"]
        )

    def test_emu_flash_with_strapping_mode_set_to_0x0f(self):
        # given
        given_raspberry_pi_id = 1
        with self.mock_subprocess(run_return_value=given_raspberry_pi_id) as (
            mock_popen,
            _,
        ):

            # when
            result = self.runner.invoke(flash, ["--id", "1"])

        # then
        self.assertEqual(result.exit_code, 0)
        self.assertIn("0x0f", mock_popen.call_args_list[0][0][0][6])

    def test_emu_monitor_success(self):
        # given
        given_raspberry_pi_id = 1
        with self.mock_subprocess(run_return_value=given_raspberry_pi_id) as (
            _,
            mock_run,
        ):
            # when
            result = self.runner.invoke(monitor, ["--id", "1"])

        # then
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_with(
            ["idf.py", "monitor", "-p", "socket://localhost:0000"]
        )

    def test_emu_monitor_with_strapping_mode_set_to_0x02(self):
        # given
        given_raspberry_pi_id = 1
        with self.mock_subprocess(run_return_value=given_raspberry_pi_id) as (
            mock_popen,
            _,
        ):
            # when
            result = self.runner.invoke(monitor, ["--id", "1"])

        # then
        self.assertEqual(result.exit_code, 0)
        self.assertIn("0x02", mock_popen.call_args_list[0][0][0][6])

    def test_emu_rgpio_success(self):
        # given
        given_raspberry_pi_id = 1
        with self.mock_subprocess(run_return_value=given_raspberry_pi_id) as (
            _,
            mock_run,
        ):
            # when
            result = self.runner.invoke(rgpio)

        # then
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_with(
            ["sudo", "docker", "exec", "-t", 1, "/usr/local/bin/detect_gpio_changes"]
        )

    def test_emu_ssh_success(self):
        # given
        given_raspberry_pi_id = 1
        with self.mock_subprocess(run_return_value=given_raspberry_pi_id) as (
            _,
            mock_run,
        ):
            # when
            result = self.runner.invoke(ssh)

        # then
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_with(
            [
                "ssh",
                "-p",
                "2222",
                "-o",
                "UserKnownHostsFile=/dev/null",
                "-o",
                "StrictHostKeyChecking=no",
                "pi@localhost",
            ]
        )

    def test_emu_esocket_success(self):
        # given
        given_raspberry_pi_id = 1
        with self.mock_subprocess(run_return_value=given_raspberry_pi_id) as (
            _,
            mock_run,
        ):
            # when
            result = self.runner.invoke(esocket, ["--id", "1"])

        # then
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_with(["nc", "localhost", "0000"])
