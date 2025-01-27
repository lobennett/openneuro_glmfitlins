## Set up docker 

For improved reproducibility, fitlins recommends using singularity containers which are reproducibile environments (singularity)[https://fitlins.readthedocs.io/en/latest/installation.html#singularity-container]

In my case, I installed docker desktop for Mac with Apple Silicon via the (docker website)[https://docs.docker.com/desktop/setup/install/mac-install/], which was about a 1.8GB application.

After installing docker desktop and completing setup via the prompts, ran the following to setup fitlins v0.11.0

docker pull poldracklab/fitlins:0.11.0

It took approximately 45 seconds to complete, specifying "Status: Downloaded newer image for poldracklab/fitlins:0.11.0
"


