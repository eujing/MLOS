import pytest

from mlos_bench.environment.azure.azure_services import AzureVMService

@pytest.fixture
def azure_vm_service():
    service = AzureVMService(config={
        "deployTemplatePath": "./mlos_bench/config/azure/azuredeploy-ubuntu-vm.json",
        "deploymentName": "TEST_DEPLOYMENT",
        "subscription": "TEST_SUB",
        "resourceGroup": "TEST_RG",
        "accessToken": "TEST_TOKEN",
        "vmName": "dummy-vm"
    })

    return service
