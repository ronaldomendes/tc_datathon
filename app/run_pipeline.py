import argparse

from src.train import train


def main(args):
    """
    :param args:
    :return:
    """
    train(save_path=args.save_path,
          mlflow_tracking_uri=args.mlflow_tracking_uri,
          experiment_name=args.experiment_name,
          test_size=args.test_size,
          random_state=args.random_state)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Run pede data pipeline with XGBoost + MLflow")
    p.add_argument("--save_path", type=str, default=None)
    p.add_argument("--mlflow_tracking_uri", type=str, default='http://localhost:5000',
                   help="override MLflow tracking URI, else uses project_root/mlruns")
    p.add_argument("--experiment_name", type=str, default="Defasagem_XGBoost")
    p.add_argument("--test_size", type=float, default=0.2)
    p.add_argument("--random_state", type=float, default=42)
    args = p.parse_args()
    main(args)
