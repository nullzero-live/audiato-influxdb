import unittest
from unittest.mock import patch, MagicMock
from models.training_model import wandb_login, load_data, train_model, eval_model

class TestMyFunctions(unittest.TestCase):
    @patch("os.getenv")
    @patch("wandb.init")
    @patch("wandb.login")
    def test_wandb_login(self, mock_login, mock_init, mock_getenv):
        # Set up mock methods
        mock_getenv.return_value = "fake_wandb_api_key"
        mock_init.return_value = None
        mock_login.return_value = None

        # Call the function
        wandb_login()

        # Check that the mock methods were called with the correct arguments
        mock_getenv.assert_called_once_with("WANDB_API_KEY")
        mock_init.assert_called_once_with(project="influx-db-audiato", mode="disabled")
        mock_login.assert_called_once_with(key="fake_wandb_api_key")

    @patch("your_module.wandb_login")  # replace 'your_module' with the actual module name
    @patch("wandb.init")
    @patch("pandas.read_csv")
    def test_load_data(self, mock_read_csv, mock_init, mock_wandb_login):
        # Set up mock methods
        mock_read_csv.return_value = MagicMock(spec=pd.DataFrame)
        mock_init.return_value.__enter__.return_value = MagicMock()

        # Call the function
        df = load_data()

        # Check that the returned value is a DataFrame
        self.assertIsInstance(df, pd.DataFrame)

    @patch("your_module.load_data")  # replace 'your_module' with the actual module name
    @patch("your_module.eval_model")
    @patch("sklearn.model_selection.train_test_split")
    def test_train_model(self, mock_split, mock_eval_model, mock_load_data):
        # Set up mock methods
        mock_load_data.return_value = MagicMock(spec=pd.DataFrame)
        mock_split.return_value = [MagicMock(spec=pd.DataFrame)] * 4
        mock_eval_model.return_value = None

        # Call the function
        train_model(MagicMock())

        # Check that the mock methods were called
        mock_load_data.assert_called_once()
        mock_split.assert_called_once()
        mock_eval_model.assert_called()

    @patch("your_module.accuracy_score")
    @patch("your_module.calculate_metrics")
    @patch("your_module.train_model.predict")
    @patch("open", new_callable=unittest.mock.mock_open())
    def test_eval_model(self, mock_open, mock_predict, mock_calculate_metrics, mock_accuracy_score):
        # Set up mock methods
        mock_predict.return_value = MagicMock()
        mock_calculate_metrics.return_value = (0.8, 0.9, 0.7)
        mock_accuracy_score.return_value = 0.85

        # Call the function
        eval_model(MagicMock(), MagicMock(), MagicMock())

        # Check that the mock methods were called
        mock_predict.assert_called()
        mock_calculate_metrics.assert_called()
        mock_accuracy_score.assert_called()
        mock_open.assert_called_with('results.txt', 'w')

if __name__ == "__main__":
    unittest.main()
