##### Node.js
# Node.js Tutorial for Debian and Ubuntu

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What
Node.js is an open-source, cross-platform JavaScript runtime environment that enables JavaScript execution on the server side.

As system administrators, we may not write Node.js applications daily, but we frequently encounter them in various scenarios—whether running web applications, managing microservices, or troubleshooting performance issues.

### 0.1. Environment
I used Debian and Ubuntu server editions, namely Debian 12 & 13, Ubuntu 22.04 & 24.04 LTS Servers.

### 0.2. Sources

- [ChatGPT](https://chatgpt.com/)
- [Node.js](https://nodejs.org/)
- [Npm.js](https://www.npmjs.com/)
- [Deepseek](https://www.deepseek.com/)



<br>
</details>

<details markdown="1">
<summary>
1. Installation
</summary>

---

Several installation methods exist, but we'll focus on the two most common approaches.

### 1.1. Install System Packages (System-wide)

Installing distribution packages provides a stable but potentially older version of Node.js. This method installs Node.js system-wide, accessible to all users. Ideal for production environments.

Update package repositories:

```
sudo apt update
```

Install Node.js and NPM (Node Package Manager):

```
sudo apt install -y nodejs npm
```

Verify installation:

```
node -v 
npm -v 
```

### 1.2. Install Using NVM (Node Version Manager) - User-based

NVM allows installation of the latest Node.js versions on a per-user basis. This provides access to newer features while maintaining isolation from system packages. Ideal for development and testing.

Install curl (Debian 13 doesn't include it by default):

```
sudo apt update
sudo apt install -y curl
```

Download and install NVM (Node Version Manager):

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash
```

Either restart your shell or source the NVM script:

```
\. "$HOME/.nvm/nvm.sh"
```

Install the latest Node.js LTS version (22.x as of writing):

```
nvm install 22
```

Verify the installation:

```
node -v 
```

Check the active Node.js version:

```
nvm current 
```

Verify NPM version:

```
npm -v 
```

Install another version (e.g., current release 23.x):

```
nvm install 23
```

Check current active version:

```
nvm current
```

Switch to version 22:

```
nvm use 22
```

List installed versions:

```
nvm ls
```

Set version 22 as the default:

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

Create a simple JavaScript program:

```
nano hello.js
```

Fill as below:

```
console.log("Hello from Node.js!");
```

Execute the program:

```
node hello.js
```

Create a more practical example:

```
nano time.js
```

Fill as below:

```
const now = new Date();
console.log(`Time now is: ${now.toLocaleString()}`);
```

Run the program:

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

console.log(chalk.green('Success message'));
console.log(chalk.red.bold('Error message'));
console.log(chalk.blue.underline('Info message'));
console.log(chalk.yellow('Warning message'));
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

View specific package details:

```
npm list chalk
```

Check for outdated packages:

```
npm outdated
```

If you want to uninstall a package:

```
npm uninstall chalk
```

<br>
</details>



