##### Node.js
# Node.js Tutorial for Debian and Ubuntu

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What
Node.js is an open-source, cross-platform JavaScript runtime environment that allows developers to run JavaScript on the server side.

As a system administrator, we may not write Node.js applications daily, but we might encounter it in various scenarios—whether it's running a web app, managing microservices, or troubleshooting performance issues.

### 0.1. Environment
I used Debian and Ubuntu server editions, namely Debian 11 & 12, Ubuntu 22.04 & 24.04 LTS Servers.

### 0.2. Sources

- [ChatGPT](https://chatgpt.com/)   
- [Node.js](https://nodejs.org/)   
- [Npm.js](https://www.npmjs.com/)   
- [Deepseek](https://www.deepseek.com/)   



<br>
</details>

<details markdown="1">
<summary>
1. Installation and Configuration Files
</summary>

---

There might be a lot of installation options but I'd like to concentrate on 2 of them.

### 1.1. Install Debian (Ubuntu) Packages - System wide

Installing the default packages of the distribution. Packages may be (actually definitely) old. So you will have old (but stable) Node.js. It can be used by all the users. Ideal for running a production site.

Update repositories

```
sudo apt update
```

Install Node.js and NPM (Node Package Manager)

```
sudo apt install -y nodejs npm
```

Verify the Node.js and Npm versions:

```
node -v 
npm -v 
```

### 1.2. Install With NVM (Node Version Manager) - User based

Downloading and installing the latest stable package. Only your user will be able to use Node.js, still stable but of course not as stable as the Debian package. Ideal for testing or developing purposes.


Install curl (Debian 12 doesn't have it by default)

```
sudo apt update
sudo apt install -y curl
```

Download and install nvm (node version manager):

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash
```

Either restart the shell or run:

```
\. "$HOME/.nvm/nvm.sh"
```

Download and install latest stable Node.js:

```
nvm install 22
```

Verify the Node.js version:

```
node -v 
```

See the active Node.js version

```
nvm current 
```

Verify NPM (Node Package Manager) version:

```
npm -v 
```

Nvm allows installing more than 1 versions of node.js.
Lets install version 23 (non LTS)

```
nvm install 23
```

See current active version

```
nvm current
```

Change to version 22 

```
nvm use 22
```

List installed versions

```
nvm ls
```

Set 22 as the default version

```
nvm alias default 22
```

Remove version 23

```
nvm uninstall 23
```

<br>
</details>

<details markdown="1">
<summary>
2. Using Node.js
</summary>

---

### 2.1. Running Javascript Programs

Let's write a simple JavaScript program:

```
nano hello.js
```

Fill as below:

```
console.log("Hello from Node.js!");
```

Run it:

```
node hello.js
```

Let's write another one:

```
nano time.js
```

Fill as below:

```
const now = new Date();
console.log(`Time now is: ${now.toLocaleString()}`);
```

Run it:

```
node time.js
```

### 2.2. Installing/Running Packages

You can install/run packages from ```https://www.npmjs.org/```

Run a package without permanently installing. It asks to install, you can say Y.

```
npm exec cowsay "Hello world"
```

Install a package locally, we'll use it in a script

```
npm install chalk@4
```

Saved to ./node_modules/

Let's use it in a script

```
nano chalktest.js
```

Fill as below:

```
const chalk = require('chalk');
console.log(chalk.green('Hello from Node.js!'));
```

Run it:

```
node chalktest.js
```

Update installed packages:

```
npm update
```

List locally installed packages:

```
npm list
```

If you want to uninstall a package:

```
npm uninstall chalk
```

<br>
</details>


