# **GitHub Copilot**: Conheça, Aprenda e Use em um Projeto Real do Zero em 15 Minutos 🚀

<div align="center">
  <img src="copilot.png" width="240" height="240" style="">
</div>

## Bem-vindxs!

Nessa introdução rápida ao GitHub Copilot veremos:

- [**GitHub Copilot**: Conheça, Aprenda e Use em um Projeto Real do Zero em 15 Minutos 🚀](#github-copilot-conheça-aprenda-e-use-em-um-projeto-real-do-zero-em-15-minutos-)
  - [Bem-vindxs!](#bem-vindxs)
  - [🫡 Conheça o Instrutor:](#-conheça-o-instrutor)
  - [🔎 Introdução ao GitHub Copilot](#-introdução-ao-github-copilot)
  - [👨‍💻 Mão na Massa](#-mão-na-massa)
  - [🧐 Experiência Pessoal](#-experiência-pessoal)
  - [👽 Futuro](#-futuro)
  - [📋 Conclusão](#-conclusão)
  - [🤓 Material Complementar](#-material-complementar)

## 🫡 Conheça o Instrutor:

<div align="center">
  <strong>Ivan Nicola Viragine</strong> - <a href="https://www.linkedin.com/in/ivan-viragine/">LinkedIn</a> | <a href="https://github.com/ivanviragine">GitHub</a>
    
</div>
</br >
<div align="center">
  <img src="ivan.jpeg" width="120" height="120" style="border-radius: 50%;">
</div>
</br >

- MBA em Ciência de Dados pela USP
- Bacharel em Ciência da Computação pela UNESP
- Engenheiro de IA, Cientista de Dados, Desenvolvedor Full Stack, Fundador de startup, etc.
- 16 anos de experiência em desenvolvimento de software
- 8 anos de experiência com Inteligência Artificial
- Atualmente AI Engineer em uma startup da Califórnia

## 🔎 Introdução ao GitHub Copilot

**O que é?**

- IA assistente de código / AI pair programmer
- LLM (Large Language Model) treinada para completar e sugerir código

**Quem está por trás?**

- GitHub, Microsoft e OpenAI

**Algumas estatísticas:**

- "Entre 60-75% dos desenvolvedores se sentem mais satisfeitos com o trabalho, menos frustrados ao codificar e conseguem se concentrar em tarefas mais satisfatórias ao usar o GitHub Copilot."
- "Desenvolvedores relataram que o GitHub Copilot os ajudou a se manterem no fluxo (73%) e a preservar o esforço mental durante tarefas repetitivas (87%)."

**Como foi treinado?**

- Modelo inicialmente desenvolvido pela OpenAI em 2021 com o nome de Codex, baseado no GPT-3.
- Treinado em diversos repositórios do GitHub e outros.
- Em novembro de 2023 passou a utilizar GPT-4.

**Principais Features:**

- Completar e sugerir código utilizando contexto (comentários, variáveis, funções, etc).
- Responder questões gerais sobre dev, em diversas línguas (Chat).
- Suporte a diversas linguagens de programação.
- Gerar documentação.
- Gerar testes (unit).
- Gerar boilerplate.
- Explicar e problemas e error stacks (e sugerir fixes).
- Code refactoring and improvements

**Exemplos:**

- Validador de CPF:

<video controls src="exemplo1_cpf.mp4" title="Validador de CPF"></video>

- Remover máscara de CPF (contexto):

<video controls src="exemplo2_cpf.mp4" title="Remover máscara de CPF (contexto)"></video>

- Acessando dataset da Internet e plotando gráfico (inline):

<video controls src="exemplo2_titanic.mp4" title="Acessando dataset da Internet e plotando gráfico (inline)"></video>

- Explicando e corrigindo erro:

<video controls src="exemplo3_titanic.mp4" title="Explicando e corrigindo erro"></video>

- Explicando função:

<video controls src="exemplo4_titanic_explain.mp4" title="Explicando função"></video>

- Empacotando em Docker (Chat):

<video controls src="exemplo5_docker_chat.mp4" title="Empacotando em Docker (Chat)"></video>

## 👨‍💻 Mão na Massa

Vamos fazer um projeto em Python, Streamlit, Poetry, Docker e Docker Compose inteiramente com o GitHub Copilot.

O projeto irá comparar dados de 2 ações da bolsa de valores.

## 🧐 Experiência Pessoal

**Onde o Copilot é útil?** 👍

- Tarefas repetitivas de fácil/média identificação de padrões
- Problemas comuns (DSA, CRUD, etc)
- Chat: você pode conversar com o Copilot, tirar dúvidas de dev, brainstorm (básico) e etc.
- Identificação e ajuda para corrigir erros
- Interpretar e explicar stacks de erro
- Gerar pequenos scripts (revise bem e não execute *rm*! 😅)

**Onde o Copilot não é tão útil?** 👎

- Chamar funções externas (fora do contexto)
- Funções complexas
- Linguagens menos populares

**Outras Ferramentas:**

- [ChatGPT (GPT-4 ou GPT-4o) - para problemas mais complexos](https://chat.openai.com/)
- [CodeGemma - Modelo aberto da Google](https://huggingface.co/google/codegemma-7b)
- [CodeLlama - Modelo aberto da  Meta](https://github.com/meta-llama/codellama)
- [CodeGPT - Plugin para modelos abertos e offline](https://codegpt.co/)

## 👽 Futuro

- **Extensions**: Integração com ferramentas como Sentry para interação utilizando linguagem natural, sem sair da IDE.
  - "Me resume os últimos incidentes" 😎
- **Workspace**: Ambiente de desenvolvimento integrado, da issue até o código e commit.

## 📋 Conclusão

- GitHub Copilot é um copiloto, não piloto!
- Aumenta sua produtividade em tarefas do dia a dia.
- Como toda LLM, pode e vai alucinar: **sempre revise o código gerado**.
- Use o Chat para pequenos problemas e dúvidas.
- Para problemas mais complexos, com muito contexto e/ou aprender algo, discutir arquitetura, provavelmente o GPT-4o será melhor.

## 🤓 Material Complementar

- [GitHub Copilot](https://github.com/features/copilot)
- [Dicas de como usar](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)
- [Prompt Engineering](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [Mais dicas e Prompt Engineering](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Mais Prompt Engineering (sim, é importantíssimo)](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/)
- [Case Duolingo](https://github.com/customer-stories/duolingo)
- [GitHub Copilot Blog](https://github.blog/tag/github-copilot/)