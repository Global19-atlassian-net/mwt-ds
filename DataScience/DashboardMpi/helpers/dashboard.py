import sys
sys.path.append("..")
import dashboard_utils

def create(path, env, commands, enable_sweep):
    d = {}
    for log_path in env.local_logs_provider.list():
        predictions = env.predictions_provider.list(log_path)
        d = dashboard_utils.create_stats(log_path, d, predictions, is_summary=True, report_progress=False)
    dashboard_utils.output_dashboard_data(d, path, commands)
