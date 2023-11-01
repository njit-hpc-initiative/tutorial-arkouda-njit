# Windows steps to install Chapel

### Install Ubuntu and initial steps to install chapel 
    
- **Create a new folder**  
    - Clone the files from GitHub [arkouda](https://github.com/Bears-R-Us/arkouda) and [arkouda-njit](https://github.com/Bears-R-Us/arkouda-njit) and save them in a folder called RESEARCH in the C-drive / desktop (anywhere where you will remember the path.) 
        
    - Download [chapel](https://github.com/chapel-lang/chapel/releases/download/1.28.0/chapel-1.28.0.tar.gz)

    - Install [Ubuntu-WSL](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#2-install-wsl/)

    - Activate/make your Linux account and open the ubuntu terminal 

    - Type bash in the terminal 
       - bash is all set to be used! 

    - Now, Use the commands on the [chapel-tutorial](https://chapel-lang.org/docs/usingchapel/QUICKSTART.html) instructions to unzip the file extract and run chapel on the terminal

### Detailed steps to install Chapel: 

- After cloning the folders, cd into the directory where chapel-1.28.0.tar.gz file is located 
    - Extract chapel using - `tar xzf chapel-1.28.0.tar.gz` 
    - Then, Type command ```source util/quickstart/setchplenv.bash```
        - This is same as this [link](https://chapel-lang.org/docs/usingchapel/QUICKSTART.html) 
    - Next, type **make**  
        - Chapel is built




# MAC steps to install Chapel, Arkouda and Arachne.

-   **Create a new folder.** (ex. Tutorial)
    -   Clone [arkouda](https://github.com/Bears-R-Us/arkouda), [arkouda-njit](https://github.com/Bears-R-Us/arkouda-njit), and download [chapel](https://github.com/chapel-lang/chapel/releases/download/1.28.0/chapel-1.28.0.tar.gz), and have them all in the Tutorial folder.

-   **Download and install [Anaconda3](https://www.anaconda.com/products/distribution)** (make sure that you check the add to **PATH** option)
    -   To ensure that Anacona3 is in your PATH, open your terminal and type conda. The output should be all of the different commands on how to use Anaconda.

    -   Open Anaconda

        -   On the left hand side click on **Environments**.
        -   Click **import**
            -   Import from Local Drive (navigate to your Tutorial
                folder, then to arkouda folder and then select the
                **arkouda-env-dev.yml** file and click open.)
            -   Name it **arkouda-env-dev**
            -   Import.
-   **Open VS code or any other source-code editor**
    -   In your source-code editor open the Tutorial folder.
    -   Navigate to the arkouda folder (/Tutorial/arkouda/util/) and create a new file called **Makefile.paths**
    -   In this new file, type this line of code.
        -   ```\$(eval \$(call add-path,/PATH to Anaconda/envs/arkouda-env-dev/))```

    - Open your terminal and type where conda. At the very end of the output, there will be a path to anaconda3. ```(ex./Users/dpetrovikj/opt/anaconda3/condabin/conda)```
    - Copy only this path ```/Users/dpetrovikj/opt/anaconda3/```, and replace it with **PATH to Anaconda** in the Makefile.paths file

    - The final command should look like this.

    - ```$(eval $(cal add-path,/Users/dpetrovikj/opt/anaconda3/envs/arkouda-env-dev/))```
                
    - Save this file. (make sure that there is no space between any of the characters)

-   **Build Chapel**
    -   Open your source-code editor and navigate to your chapel folder, more specifically in CHPL\_HOME/util/quickstart/setchplenv.bash
    
    -   Go to line 64 & 65 and comment out the code.
        -   Ex. ```# echo "Setting CHPL\_RE2 to none"```
        -   Ex. ```# export CHPL\_RE2=none```
    -   Open your terminal and cd into the Tutorial folder.
    -   Extract chapel - ```tar xzf chapel-1.28.0.tar.gz```
    -   Then cd into that folder and run the command ```source util/quickstart/setchplenv.bash```
    -   Then run the command ```make```
    -   Now chapel should be built and in order to check if you did everything correctly run this command on your terminal
        -   ```chpl examples/hello3-datapar.chpl```
