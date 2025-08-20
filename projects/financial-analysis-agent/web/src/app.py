import streamlit as st
import requests
import json
from typing import Dict, Any
import os

# Configuração da página
st.set_page_config(
    page_title="Financial Analysis Agent",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configurações
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Título da aplicação
st.title(" Financial Analysis Agent")
st.markdown("Sistema inteligente de análise financeira usando IA")

# Sidebar para configurações
st.sidebar.header("⚙️ Configurações")

# Seleção do tipo de análise
analysis_type = st.sidebar.selectbox(
    "Tipo de Análise",
    ["análise fundamentalista", "análise técnica", "análise de risco", "análise completa"]
)

# Input para ticker
ticker = st.text_input(" Digite o código da ação (ex: PETR4, VALE3)", "PETR4").upper()

# Input para informações da empresa (se análise de risco)
company_info = ""
if analysis_type == "análise de risco":
    company_info = st.sidebar.text_area("ℹ️ Informações da empresa (opcional)", "")

# Botão para executar análise
if st.button("�� Executar Análise", type="primary"):
    if ticker:
        with st.spinner(f"Executando {analysis_type} para {ticker}..."):
            try:
                # Preparar dados da requisição
                data = {
                    "ticker": ticker,
                    "analysis_type": analysis_type,
                    "company_info": company_info
                }

                # Determinar endpoint baseado no tipo de análise
                if analysis_type == "análise fundamentalista":
                    endpoint = "/analyze/fundamental"
                elif analysis_type == "análise técnica":
                    endpoint = "/analyze/technical"
                elif analysis_type == "análise de risco":
                    endpoint = "/analyze/risk"
                else:  # análise completa
                    endpoint = "/analyze/comprehensive"

                # Fazer requisição para a API
                response = requests.post(
                    f"{API_URL}{endpoint}",
                    json=data,
                    timeout=120
                )

                if response.status_code == 200:
                    result = response.json()

                    if result["success"]:
                        st.success("✅ Análise concluída com sucesso!")

                        # Mostrar resultados
                        analysis_data = result["data"]

                        # Informações básicas
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Ticker", analysis_data["ticker"])
                        with col2:
                            st.metric("Tipo", analysis_data["analysis_type"])
                        with col3:
                            if "current_price" in analysis_data:
                                st.metric("Preço", analysis_data["current_price"])

                        # Análise detalhada
                        if "detailed_analysis" in analysis_data:
                            st.subheader("📋 Análise Detalhada")
                            st.write(analysis_data["detailed_analysis"])

                        # Resumo executivo
                        if "executive_summary" in analysis_data:
                            st.subheader("📊 Resumo Executivo")
                            st.write(analysis_data["executive_summary"])

                        # Análise técnica
                        if "technical_analysis" in analysis_data:
                            st.subheader(" Análise Técnica")
                            st.write(analysis_data["technical_analysis"])

                        # Análise de risco
                        if "risk_analysis" in analysis_data:
                            st.subheader("⚠️ Análise de Risco")
                            st.write(analysis_data["risk_analysis"])

                        # Resumo contextual
                        if "contextual_summary" in analysis_data:
                            st.subheader("🌍 Resumo Contextual")
                            st.write(analysis_data["contextual_summary"])

                    else:
                        st.error(f"❌ Erro na análise: {result.get('error', 'Erro desconhecido')}")
                else:
                    st.error(f"❌ Erro na API: {response.status_code}")

            except Exception as e:
                st.error(f"❌ Erro durante a execução: {str(e)}")
    else:
        st.warning("⚠️ Por favor, digite um código de ação válido.")

# Seção para perguntas gerais
st.markdown("---")
st.subheader("💬 Perguntas Gerais")

question = st.text_input("Faça uma pergunta sobre o mercado financeiro:")
if st.button("🤔 Perguntar"):
    if question:
        with st.spinner("Processando pergunta..."):
            try:
                response = requests.post(
                    f"{API_URL}/agent/ask",
                    json={"question": question},
                    timeout=60
                )

                if response.status_code == 200:
                    result = response.json()
                    if result["success"]:
                        st.success("✅ Pergunta respondida!")
                        st.write(result["data"]["answer"])
                    else:
                        st.error(f"❌ Erro: {result.get('error', 'Erro desconhecido')}")
                else:
                    st.error(f"❌ Erro na API: {response.status_code}")

            except Exception as e:
                st.error(f"❌ Erro: {str(e)}")
    else:
        st.warning("⚠️ Por favor, digite uma pergunta.")

# Footer
st.markdown("---")
st.markdown("🔧 Desenvolvido com LangChain e OpenAI")
