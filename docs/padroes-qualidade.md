# 🏆 PADRÕES DE QUALIDADE - IA-ML-KNOWLEDGE-BASE

## 🎯 VISÃO GERAL

Este documento define os padrões de qualidade obrigatórios para todos os projetos do IA Knowledge Base, garantindo código profissional, escalável e mantível.

---

## 🔧 FERRAMENTAS OBRIGATÓRIAS

### **Formatação e Linting**
```bash
# Formatação automática
black --line-length 120 --target-version py39 .

# Organização de imports
isort --profile black --line-length 120 .

# Linting
flake8 --max-line-length 120 --extend-ignore E203,W503 .

# Type checking
mypy --ignore-missing-imports --disallow-untyped-defs .
```

### **Testes**
```bash
# Testes com pytest
pytest --cov=src --cov-report=html --cov-report=term-missing

# Testes de integração
pytest tests/integration/ -v
```

---

## 📁 ESTRUTURA DE PROJETO PROFISSIONAL

### **Template Padrão**
```
project-name/
│
├── README.md                    # Documentação principal
├── docs/                        # Documentação técnica
│   ├── api-specification.md     # OpenAPI/Swagger docs
│   ├── architecture.md          # Arquitetura do sistema
│   ├── deployment.md            # Guia de deploy
│   └── contributing.md          # Padrões de contribuição
│
├── src/
│   ├── __init__.py
│   ├── main.py                  # Entry point FastAPI
│   ├── api/                     # Rotas da API
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── health.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       └── endpoints.py
│   │   ├── dependencies.py      # Dependency injection
│   │   └── middleware.py        # Custom middleware
│   ├── core/                    # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── config.py            # Configuration management
│   │   ├── models/              # Pydantic models
│   │   │   ├── __init__.py
│   │   │   ├── requests.py
│   │   │   └── responses.py
│   │   └── services/            # Business logic
│   │       ├── __init__.py
│   │       └── main_service.py
│   ├── utils/                   # Utilitários
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── helpers.py
│   └── tests/                   # Testes
│       ├── __init__.py
│       ├── unit/
│       │   ├── __init__.py
│       │   └── test_services.py
│       ├── integration/
│       │   ├── __init__.py
│       │   └── test_api.py
│       └── fixtures/
│           ├── __init__.py
│           └── test_data.py
│
├── models/                      # Modelos ML salvos
├── data/                        # Dados de exemplo
├── configs/                     # Configurações
├── scripts/                     # Scripts utilitários
├── docker/                      # Docker configs
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── docker-compose.prod.yml
│
├── .github/                     # GitHub Actions
│   └── workflows/
│       ├── ci.yml
│       ├── cd.yml
│       └── quality-check.yml
│
├── requirements/                 # Dependências organizadas
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
│
├── .pre-commit-config.yaml      # Pre-commit hooks
├── pyproject.toml              # Config tools (black, isort, etc)
├── pytest.ini                  # Config pytest
├── mypy.ini                    # Config mypy
└── .env.example                # Exemplo de variáveis
```

---

## 📝 PADRÕES DE CÓDIGO

### **1. Imports Organizados**
```python
# Standard library imports
import logging
import os
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

# Third-party imports
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from redis import Redis

# Local imports
from src.core.config import settings
from src.core.models.requests import DataRequest
from src.core.services.data_service import DataService
from src.utils.validators import validate_data
```

### **2. Type Hints Obrigatórios**
```python
from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from uuid import UUID

def process_data(
    data: List[Dict[str, Any]],
    operation: str,
    config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Process data with specified operation.
    
    Args:
        data: Input data to process
        operation: Type of operation to perform
        config: Optional configuration parameters
        
    Returns:
        Processed data with metadata
        
    Raises:
        ValueError: If operation is not supported
        ProcessingError: If data processing fails
    """
    pass

class DataService:
    """Service for data processing operations."""
    
    def __init__(self, redis_client: Redis) -> None:
        """Initialize data service.
        
        Args:
            redis_client: Redis client for caching
        """
        self.redis_client = redis_client
    
    async def process_batch(
        self,
        data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Process batch of data items.
        
        Args:
            data: List of data items to process
            
        Returns:
            List of processed data items
        """
        pass
```

### **3. Pydantic Models**
```python
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime

class DataRequest(BaseModel):
    """Request model for data processing.
    
    Attributes:
        data: Input data to process
        operation: Type of operation to perform
        config: Optional configuration parameters
    """
    data: List[Dict[str, Any]] = Field(..., description="Input data")
    operation: str = Field(..., description="Processing operation")
    config: Optional[Dict[str, Any]] = Field(None, description="Configuration")
    
    @validator('operation')
    def validate_operation(cls, v: str) -> str:
        """Validate operation type."""
        allowed_operations = ['clean', 'normalize', 'validate', 'transform']
        if v not in allowed_operations:
            raise ValueError(f"Operation must be one of {allowed_operations}")
        return v
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "data": [{"id": 1, "value": 10.5}],
                "operation": "normalize",
                "config": {"method": "zscore"}
            }
        }

class DataResponse(BaseModel):
    """Response model for data processing."""
    processed_data: List[Dict[str, Any]] = Field(..., description="Processed data")
    metadata: Dict[str, Any] = Field(..., description="Processing metadata")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    processing_time: float = Field(..., description="Processing time in seconds")
```

### **4. FastAPI Endpoints**
```python
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["data"])

@router.post("/process", response_model=DataResponse)
async def process_data(
    request: DataRequest,
    background_tasks: BackgroundTasks,
    data_service: DataService = Depends(get_data_service)
) -> DataResponse:
    """Process data with specified operation.
    
    Args:
        request: Data processing request
        background_tasks: FastAPI background tasks
        data_service: Injected data service
        
    Returns:
        Processed data response
        
    Raises:
        HTTPException: If processing fails
    """
    try:
        logger.info(f"Processing data with operation: {request.operation}")
        
        # Process data
        result = await data_service.process_batch(request.data)
        
        # Add background task for logging
        background_tasks.add_task(log_processing_result, request.operation, len(result))
        
        return DataResponse(
            processed_data=result,
            metadata={"operation": request.operation, "items_processed": len(result)},
            processing_time=0.5  # Calculate actual time
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Processing error: {e}")
        raise HTTPException(status_code=500, detail="Internal processing error")

@router.get("/health")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint.
    
    Returns:
        Health status information
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }
```

### **5. Services (Lógica de Negócio)**
```python
from typing import List, Dict, Any, Optional
import asyncio
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class DataService:
    """Service for data processing operations."""
    
    def __init__(self, redis_client: Redis) -> None:
        """Initialize data service.
        
        Args:
            redis_client: Redis client for caching
        """
        self.redis_client = redis_client
        self._cache_ttl = 3600  # 1 hour
    
    async def process_batch(
        self,
        data: List[Dict[str, Any]],
        operation: str,
        config: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Process batch of data items.
        
        Args:
            data: List of data items to process
            operation: Type of operation to perform
            config: Optional configuration parameters
            
        Returns:
            List of processed data items
            
        Raises:
            ProcessingError: If processing fails
        """
        try:
            # Check cache first
            cache_key = self._generate_cache_key(data, operation, config)
            cached_result = await self._get_from_cache(cache_key)
            
            if cached_result:
                logger.info(f"Returning cached result for operation: {operation}")
                return cached_result
            
            # Process data
            processed_data = await self._process_data(data, operation, config)
            
            # Cache result
            await self._cache_result(cache_key, processed_data)
            
            logger.info(f"Successfully processed {len(processed_data)} items")
            return processed_data
            
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            raise ProcessingError(f"Failed to process data: {e}")
    
    async def _process_data(
        self,
        data: List[Dict[str, Any]],
        operation: str,
        config: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Internal method for data processing."""
        if operation == "clean":
            return await self._clean_data(data, config)
        elif operation == "normalize":
            return await self._normalize_data(data, config)
        elif operation == "validate":
            return await self._validate_data(data, config)
        else:
            raise ValueError(f"Unsupported operation: {operation}")
    
    async def _clean_data(
        self,
        data: List[Dict[str, Any]],
        config: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Clean data by removing nulls and duplicates."""
        # Implementation here
        pass
    
    async def _normalize_data(
        self,
        data: List[Dict[str, Any]],
        config: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Normalize data using specified method."""
        # Implementation here
        pass
    
    async def _validate_data(
        self,
        data: List[Dict[str, Any]],
        config: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Validate data against schema."""
        # Implementation here
        pass
    
    def _generate_cache_key(
        self,
        data: List[Dict[str, Any]],
        operation: str,
        config: Optional[Dict[str, Any]] = None
    ) -> str:
        """Generate cache key for data processing."""
        # Implementation here
        pass
    
    async def _get_from_cache(self, key: str) -> Optional[List[Dict[str, Any]]]:
        """Get result from cache."""
        # Implementation here
        pass
    
    async def _cache_result(
        self,
        key: str,
        data: List[Dict[str, Any]]
    ) -> None:
        """Cache processing result."""
        # Implementation here
        pass
```

---

## 🧪 PADRÕES DE TESTE

### **1. Testes Unitários**
```python
import pytest
from unittest.mock import Mock, patch, AsyncMock
from typing import List, Dict, Any

from src.core.services.data_service import DataService
from src.core.models.requests import DataRequest

class TestDataService:
    """Test cases for DataService."""
    
    @pytest.fixture
    def mock_redis(self) -> Mock:
        """Mock Redis client."""
        return Mock()
    
    @pytest.fixture
    def data_service(self, mock_redis: Mock) -> DataService:
        """DataService instance with mocked dependencies."""
        return DataService(mock_redis)
    
    @pytest.fixture
    def sample_data(self) -> List[Dict[str, Any]]:
        """Sample data for testing."""
        return [
            {"id": 1, "value": 10.5, "category": "A"},
            {"id": 2, "value": 20.3, "category": "B"},
            {"id": 3, "value": None, "category": "A"}
        ]
    
    def test_data_service_initialization(self, mock_redis: Mock) -> None:
        """Test DataService initialization."""
        service = DataService(mock_redis)
        assert service.redis_client == mock_redis
        assert service._cache_ttl == 3600
    
    @pytest.mark.asyncio
    async def test_process_batch_clean_operation(
        self,
        data_service: DataService,
        sample_data: List[Dict[str, Any]]
    ) -> None:
        """Test batch processing with clean operation."""
        # Arrange
        operation = "clean"
        config = {"remove_nulls": True}
        
        # Act
        result = await data_service.process_batch(sample_data, operation, config)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 2  # One item with None value should be removed
        assert all("value" in item and item["value"] is not None for item in result)
    
    @pytest.mark.asyncio
    async def test_process_batch_invalid_operation(
        self,
        data_service: DataService,
        sample_data: List[Dict[str, Any]]
    ) -> None:
        """Test batch processing with invalid operation."""
        # Arrange
        operation = "invalid_operation"
        
        # Act & Assert
        with pytest.raises(ValueError, match="Unsupported operation"):
            await data_service.process_batch(sample_data, operation)
    
    @pytest.mark.asyncio
    async def test_cache_integration(
        self,
        data_service: DataService,
        sample_data: List[Dict[str, Any]]
    ) -> None:
        """Test cache integration."""
        # Arrange
        operation = "clean"
        data_service.redis_client.get = AsyncMock(return_value=None)
        data_service.redis_client.setex = AsyncMock()
        
        # Act
        await data_service.process_batch(sample_data, operation)
        
        # Assert
        data_service.redis_client.get.assert_called_once()
        data_service.redis_client.setex.assert_called_once()
```

### **2. Testes de Integração**
```python
import pytest
from fastapi.testclient import TestClient
from typing import Dict, Any

from src.main import app
from src.core.models.requests import DataRequest

class TestDataAPI:
    """Integration tests for data API."""
    
    @pytest.fixture
    def client(self) -> TestClient:
        """Test client for FastAPI app."""
        return TestClient(app)
    
    @pytest.fixture
    def sample_request_data(self) -> Dict[str, Any]:
        """Sample request data for testing."""
        return {
            "data": [
                {"id": 1, "value": 10.5, "category": "A"},
                {"id": 2, "value": 20.3, "category": "B"}
            ],
            "operation": "clean",
            "config": {"remove_nulls": True}
        }
    
    def test_health_check(self, client: TestClient) -> None:
        """Test health check endpoint."""
        # Act
        response = client.get("/health")
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert "version" in data
    
    def test_process_data_success(
        self,
        client: TestClient,
        sample_request_data: Dict[str, Any]
    ) -> None:
        """Test successful data processing."""
        # Act
        response = client.post("/api/v1/process", json=sample_request_data)
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "processed_data" in data
        assert "metadata" in data
        assert "timestamp" in data
        assert "processing_time" in data
    
    def test_process_data_invalid_operation(
        self,
        client: TestClient,
        sample_request_data: Dict[str, Any]
    ) -> None:
        """Test data processing with invalid operation."""
        # Arrange
        sample_request_data["operation"] = "invalid_operation"
        
        # Act
        response = client.post("/api/v1/process", json=sample_request_data)
        
        # Assert
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "invalid_operation" in data["detail"]
    
    def test_process_data_empty_data(
        self,
        client: TestClient,
        sample_request_data: Dict[str, Any]
    ) -> None:
        """Test data processing with empty data."""
        # Arrange
        sample_request_data["data"] = []
        
        # Act
        response = client.post("/api/v1/process", json=sample_request_data)
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["processed_data"] == []
```

---

## 📊 CONFIGURAÇÕES

### **1. pyproject.toml**
```toml
[tool.black]
line-length = 120
target-version = ['py39']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

[tool.isort]
profile = "black"
line_length = 120
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--cov=src",
    "--cov-report=html",
    "--cov-report=term-missing",
    "--cov-fail-under=80"
]
```

### **2. pytest.ini**
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --strict-config
    --cov=src
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow running tests
    e2e: End-to-end tests
```

### **3. mypy.ini**
```ini
[mypy]
python_version = 3.9
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
warn_unreachable = True
strict_equality = True

[mypy.plugins.pydantic.*]
init_forbid_extra = True
init_typed = True
warn_required_dynamic_aliases = True
warn_untyped_fields = True
```

---

## 📈 MÉTRICAS DE QUALIDADE

### **Quantitativas:**
- **Cobertura de Testes:** > 90%

### **Qualitativas:**
- ✅ Código legível e bem documentado
- ✅ Arquitetura limpa e escalável
- ✅ Tratamento de erros robusto
- ✅ Logs estruturados e informativos
- ✅ Configuração externalizada
- ✅ Testes abrangentes e confiáveis

---

## 🎯 CHECKLIST DE QUALIDADE

### **Antes do Commit:**
- [ ] Código formatado com Black
- [ ] Imports organizados com isort
- [ ] Type hints completos
- [ ] Docstrings em inglês
- [ ] Testes passando
- [ ] Cobertura > 90%
- [ ] Linting sem erros

---

*Estes padrões garantem qualidade profissional e facilitam manutenção e evolução dos projetos.* 