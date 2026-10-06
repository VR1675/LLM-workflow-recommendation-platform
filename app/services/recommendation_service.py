import torch
import torch.nn.functional as F


class RecommendationEngine:
    def __init__(self):
        self.recommendation_catalog = [
            "Auto-classify incoming support tickets",
            "Route high-priority workflows to escalation queues",
            "Generate AI-assisted workflow summaries",
            "Monitor workflow failures using retry tracking",
            "Recommend automation steps based on user intent",
            "Suggest automated customer response templates",
            "Trigger analytics workflow for reporting insights",
            "Detect workflow anomalies using monitoring signals",
            "Optimize backend workflow execution latency",
            "Generate personalized next-best-action recommendations"
        ]

        self.catalog_embeddings = torch.rand(len(self.recommendation_catalog), 16)

    def _query_embedding(self, query: str):
        torch.manual_seed(len(query))
        return torch.rand(16)

    def generate_recommendations(self, query: str):
        query_embedding = self._query_embedding(query)

        similarity_scores = F.cosine_similarity(
            query_embedding.unsqueeze(0),
            self.catalog_embeddings
        )

        top_indices = torch.topk(similarity_scores, k=3).indices.tolist()

        return [self.recommendation_catalog[index] for index in top_indices]