# 🤝 GUIA DE CONTRIBUIÇÃO

> **Como contribuir para o projeto IA-ML-KNOWLEDGE-BASE**

Obrigado por considerar contribuir para o **IA-ML-KNOWLEDGE-BASE**! Este documento fornece diretrizes para contribuições.

---

## 🎯 **COMO CONTRIBUIR**

### **📋 Antes de Começar**

1. **Verifique** se já existe uma issue relacionada
2. **Leia** a documentação do projeto
3. **Familiarize-se** com os padrões de código
4. **Entenda** a estrutura do projeto

### **🚀 Processo de Contribuição**

#### **1. Fork e Clone**
```bash
# Fork o repositório no GitHub
# Clone seu fork
git clone https://github.com/SEU_USUARIO/ia-ml-knowledge-base.git
cd ia-ml-knowledge-base

# Adicione o repositório original como upstream
git remote add upstream https://github.com/LucasBiason/ia-ml-knowledge-base.git
```

#### **2. Crie uma Branch**
```bash
# Atualize sua branch main
git checkout main
git pull upstream main

# Crie uma nova branch para sua feature
git checkout -b feature/nome-da-sua-feature
```

#### **4. Desenvolva**
- **Siga** os padrões de código definidos
- **Escreva** testes para novas funcionalidades
- **Atualize** a documentação conforme necessário
- **Mantenha** commits pequenos e focados

#### **5. Teste**
```bash
# Execute os testes
pytest --cov=src --cov-report=term-missing

# Execute o linting
pre-commit run --all-files

# Verifique os tipos
mypy src/ --ignore-missing-imports
```

#### **6. Commit e Push**
```bash
# Adicione suas mudanças
git add .

# Faça commit seguindo conventional commits
git commit -m "feat: adiciona nova funcionalidade X"

# Push para seu fork
git push origin feature/nome-da-sua-feature
```

#### **7. Abra um Pull Request**
1. **Vá** para o repositório original no GitHub
2. **Clique** em "New Pull Request"
3. **Selecione** sua branch
4. **Preencha** o template do PR
5. **Aguarde** a revisão

---

## 📝 **PADRÕES DE CÓDIGO**

### **🐍 Python**

#### **Formatação**
- **Black** com linha de 120 caracteres
- **isort** para organização de imports
- **flake8** para linting
- **mypy** para type checking

#### **Imports**
```python
# Standard library
import os
import sys
from typing import List, Dict, Optional

# Third-party
import pandas as pd
import numpy as np
from fastapi import FastAPI

# Local
from src.core import processor
from src.utils import helpers
```

#### **Type Hints**
```python
def process_data(data: List[Dict[str, Any]], 
                config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Process data with given configuration.
    
    Args:
        data: Input data to process
        config: Optional configuration parameters
        
    Returns:
        Processed data with metadata
    """
    pass
```

#### **Docstrings**
```python
def analyze_sentiment(text: str, model: str = "bert") -> Dict[str, float]:
    """Analyze sentiment of given text.
    
    Args:
        text: Input text to analyze
        model: Model to use for analysis (default: "bert")
        
    Returns:
        Dictionary with sentiment scores
        
    Raises:
        ValueError: If text is empty
        ModelNotFoundError: If specified model doesn't exist
    """
    pass
```

### **📚 Documentação**

#### **Markdown**
- **Use** headers apropriados (# ## ###)
- **Inclua** exemplos de código
- **Mantenha** links atualizados
- **Use** emojis para melhor visualização

#### **README**
- **Descrição clara** do projeto
- **Instruções** de instalação
- **Exemplos** de uso
- **Badges** relevantes

---

## 🧪 **TESTES**

### **📊 Cobertura Mínima**
- **80%** para código novo
- **90%** para funcionalidades críticas

### **🎯 Tipos de Teste**
```python
# Teste unitário
def test_data_processor():
    """Test data processor functionality."""
    processor = DataProcessor()
    result = processor.process([{"id": 1, "value": 10}])
    assert result["processed"] == True

# Teste de integração
def test_api_endpoint():
    """Test API endpoint."""
    response = client.post("/api/v1/process", json={"data": [...]})
    assert response.status_code == 200
    assert "result" in response.json()

# Teste de performance
def test_large_dataset():
    """Test processing large dataset."""
    large_data = generate_test_data(10000)
    start_time = time.time()
    result = processor.process(large_data)
    assert time.time() - start_time < 5.0  # Max 5 seconds
```

---

## 📋 **CONVENTIONAL COMMITS**

### **🎯 Formato**
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### **📝 Tipos**
- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Documentação
- **style**: Formatação (não afeta código)
- **refactor**: Refatoração
- **test**: Adicionar ou corrigir testes
- **chore**: Tarefas de manutenção

### **💡 Exemplos**
```bash
feat: adiciona endpoint para análise de sentimentos
fix(api): corrige erro de validação no endpoint /health
docs: atualiza README com novos exemplos
test: adiciona testes para processamento de dados
refactor: reorganiza estrutura de pastas
```

---

## 🔍 **REVIEW PROCESS**

### **📋 Checklist do Revisor**
- [ ] **Código** segue padrões estabelecidos
- [ ] **Testes** passam e cobrem mudanças
- [ ] **Documentação** foi atualizada
- [ ] **Commits** seguem conventional commits
- [ ] **Funcionalidade** funciona conforme esperado
- [ ] **Performance** não foi degradada
- [ ] **Segurança** não foi comprometida

### **📝 Template de PR**
```markdown
## 📋 Descrição
Breve descrição das mudanças

## 🎯 Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## 🧪 Testes
- [ ] Testes unitários passam
- [ ] Testes de integração passam
- [ ] Cobertura mantida ou aumentada

## 📚 Documentação
- [ ] README atualizado
- [ ] Docstrings adicionadas
- [ ] Exemplos atualizados

## 🔍 Checklist
- [ ] Código segue padrões
- [ ] Commits seguem conventional commits
- [ ] Self-review realizado
```

---

## 🚨 **REPORTANDO BUGS**

### **📋 Template de Issue**
```markdown
## 🐛 Descrição do Bug
Descrição clara e concisa do bug

## 🔄 Para Reproduzir**
1. Vá para '...'
2. Clique em '...'
3. Role até '...'
4. Veja o erro

## ✅ Comportamento Esperado**
Descrição do que deveria acontecer

## 📸 Screenshots**
Se aplicável, adicione screenshots

## 💻 Ambiente**
- OS: [ex: Ubuntu 20.04]
- Python: [ex: 3.9.7]
- Versão: [ex: 1.0.0]

## 📋 Contexto Adicional**
Qualquer contexto adicional sobre o problema
```

---

## 💡 **SUGESTÕES DE MELHORIAS**

### **📋 Template de Feature Request**
```markdown
## 💡 Descrição da Sugestão
Descrição clara da funcionalidade desejada

## 🎯 Problema que Resolve**
Descrição do problema que esta funcionalidade resolveria

## 💭 Solução Proposta**
Descrição da solução proposta

## 🔄 Alternativas Consideradas**
Outras soluções que foram consideradas

## 📋 Contexto Adicional**
Qualquer contexto adicional
```

---

## 🏆 **RECONHECIMENTO**

### **👥 Contribuidores**
- **Contribuidores** serão listados no README
- **Mencões** em releases
- **Badges** para contribuidores ativos

### **🎯 Tipos de Contribuição**
- **Código**: Novas funcionalidades, correções
- **Documentação**: Melhorias na docs
- **Testes**: Novos testes, melhorias
- **Design**: UI/UX, mockups
- **Ideias**: Sugestões, feedback

---

## 📞 **CONTATO**

### **👤 Lucas Biason**
- **Email**: lucas.biason@foxcodesoftware.com
- **GitHub**: [@LucasBiason](https://github.com/LucasBiason)
- **LinkedIn**: [Lucas Biason](https://www.linkedin.com/in/lucas-biason-0b70a334/)

### **💬 Comunicação**
- **Issues**: Para bugs e sugestões
- **Discussions**: Para discussões gerais
- **Email**: Para assuntos privados

---

## 📄 **LICENÇA**

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [Licença MIT](LICENSE).

---

*Obrigado por contribuir para o IA Knowledge Base! 🚀* 