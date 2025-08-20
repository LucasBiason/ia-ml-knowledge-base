#!/bin/bash

echo "🚀 Deployando Financial Analysis Agent..."

if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker não está rodando. Inicie o Docker primeiro."
    exit 1
fi

if [ ! -f ".env" ]; then
    echo "❌ Arquivo .env não encontrado na raiz do projeto."
    echo "   Crie o arquivo .env com as variáveis necessárias."
    exit 1
fi

source .env

if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY não definida no arquivo .env"
    exit 1
fi

echo "✅ Variáveis de ambiente carregadas com sucesso!"

echo "📦 Construindo containers..."
docker compose build

echo "🚀 Subindo serviços..."
docker compose up -d

echo "⏳ Aguardando API estar pronta..."
until curl -f http://localhost:${API_PORT:-8000}/health > /dev/null 2>&1; do
    echo "   Aguardando API..."
    sleep 5
done

echo "✅ API está pronta!"

echo "⏳ Aguardando interface web estar pronta..."
until curl -f http://localhost:${WEB_PORT:-8501} > /dev/null 2>&1; do
    echo "   Aguardando Web..."
    sleep 5
done

echo "✅ Interface web está pronta!"

echo ""
echo "🎉 Deploy concluído com sucesso!"
echo ""
echo "📡 API REST: http://localhost:${API_PORT:-8000}"
echo " Documentação: http://localhost:${API_PORT:-8000}/docs"
echo "🌐 Interface Web: http://localhost:${WEB_PORT:-8501}"
echo ""
echo "Para parar os serviços: docker compose down"
echo "Para ver logs: docker compose logs -f"
