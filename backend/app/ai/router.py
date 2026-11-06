class AIRouter():

    def __init__(self, providers:dict):
        self.providers = providers

    def select_provider(self,provider_name:str):
        providers = self.providers.get(provider_name)
        if providers is None:
            return None
        print(providers)
        return providers


