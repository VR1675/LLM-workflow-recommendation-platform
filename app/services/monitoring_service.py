class MonitoringService:
    def __init__(self):
        self.total_workflows = 0
        self.successful_workflows = 0
        self.failed_workflows = 0
        self.total_latency = 0
        self.cache_hits = 0
        self.cache_misses = 0

    def record_workflow(self, latency_ms: int, cache_used: bool):
        self.total_workflows += 1
        self.successful_workflows += 1
        self.total_latency += latency_ms

        if cache_used:
            self.cache_hits += 1
        else:
            self.cache_misses += 1

    def record_failure(self):
        self.total_workflows += 1
        self.failed_workflows += 1

    def get_metrics(self):
        average_latency = 0
        success_rate = 0
        cache_hit_rate = 0

        if self.total_workflows > 0:
            average_latency = round(
                self.total_latency / max(self.successful_workflows, 1), 2
            )
            success_rate = round(
                (self.successful_workflows / self.total_workflows) * 100, 2
            )

        total_cache_requests = self.cache_hits + self.cache_misses

        if total_cache_requests > 0:
            cache_hit_rate = round(
                (self.cache_hits / total_cache_requests) * 100, 2
            )

        return {
            "simulated_daily_events": "250K+",
            "total_workflows_processed": self.total_workflows,
            "successful_workflows": self.successful_workflows,
            "failed_workflows": self.failed_workflows,
            "average_latency_ms": average_latency,
            "success_rate_percent": success_rate,
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "cache_hit_rate_percent": cache_hit_rate,
            "target_uptime": "99.9%",
            "monitoring_enabled": True
        }