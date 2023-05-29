## Git e Versionamento pela ADA Santander

#### Comandos Usados
### 1.  git global

- git --global user.name "Nome"
- git --global user.email "email@tal.com"
- git config --global core.editor nvim
- git init

### 2. Estados do Git

 Terminal | Tradução
 :------- | :-----
 UnTracked | Não rastreado
 UnModified | Não Modificado
 Modified | Modifiacdo
 Staged | Preparado

### 3. Comandos
- git add
- git restore arquivo.txt
- git restore --staged arq.txt
- git diff 
- git diff --staged
- git log

- git commit -m "Mensagem"
- git pull --rebase
  ou
- git feth // Não altera o código de imediato
- git diff origin/main  // visualiza as alterações e depois git pull
  
- git push -u origin main

### 4. Branch
São ramificações do git
- git branch testing  // Criando branch
- git log --oneline --decorate // indica em qual branch HEAD esta apontando
- git checkout testing // muda de branch 
para mesclar os arquivo, esteja na branch que deseja add os arquivos de outra braanch
- git checkout main
- git merge testing

