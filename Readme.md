<div align="center">
  <img src="https://user-images.githubusercontent.com/78467470/168476573-b0df52f2-c02b-4c41-abc2-46764bc7375c.png" width="100"/>
<h1 align="center">Arasaka OpenRpc</h1>
<p> A discord Rich Presence tool<p>
<img src="https://media.giphy.com/media/FVkq1PhATef2PlgMLI/giphy.gif">
</div>

<h2>Description</h2>

A discord Rpc using `pypresence` to make your profile look a lil cool and descriptive using `python`. <br>

<img src ="https://user-images.githubusercontent.com/78467470/213911315-539f74dc-6706-45ea-ba34-492fb4b07f79.png">

<h2>Installation & Configuration</h2>


- Create your account on <a href="https://discord.com/developers/applications">Discord Developer Portal.</a>
    - Click on New application.

        <img src="https://user-images.githubusercontent.com/78467470/213911573-fea212ae-b9e0-4731-b93d-39ec4cd6d9fc.png">
    - Enter the Name for your application and check terms and conditions box.

        <img src="https://user-images.githubusercontent.com/78467470/213911690-3ddc9ddc-8c14-47bf-838a-49bee93f710e.png">
        
    - On General information page you will see `application id` Copy it.

        <img src="https://user-images.githubusercontent.com/78467470/213911730-404c0a35-dcb8-4733-b5ff-eb4eb946e903.png">
    
    - Go to Bot page and click on `Add Bot`

        <img src="https://user-images.githubusercontent.com/78467470/213911816-357cdae1-0d28-4724-86ca-b4f816b5f0fc.png">
    
    - Scroll Down To `Privileged Gateway Intents` and turn on `Presence Intent`.

        <img src="https://user-images.githubusercontent.com/78467470/213911904-8be90a5c-f15e-4550-a4cb-188bcdc8c937.png">

    - Now go to Rich Presence and click on `Add Images` and add two images, name them `largeImage` and `smallImage` exactly like this.

- Considering you have `python` installed in your system.

    - Now Download this repo open the `Arasaka.py` and replace `rpc = pypresence.Presence("your application id here")` with your `application id` we copied earlier.

    - You can also replace the values of `line 19` variable `letters` with your own quotes.

    - And you are all set to use Our Rpc, Happy Coding!

<h2> To congfigure it for Auto execute everytime you open your pc without showing annoying cmd pop-up </h2>

>Lazy rn to write will provide a video soon.