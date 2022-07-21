# Why do jobs fails
After a command is executed it will return an exit status
1. 0: Job succeeded
2. 1~255: Job failed

# Use custom image
add `image` property in job

# Variables:
## Setting global variables In .gitlab-ci.yml
``` yml
variables:
  DEPLOY_ENVIRONMENT: staging
```
## Set default value and description
``` yml
variables:
  DEPLOY_ENVIRONMENT:
    value: "staging"
    description: "The deployment target."
```

# Cache

# environment


# menual trigger
``` yml
when: manual
allow_failure: false
```

# Predefined environment variables
https://docs.gitlab.com/ee/ci/variables/predefined_variables.html
``` yml
build website:
  script:
    - echo $CI_COMMIT_SHORT_SHA
```

# Trigger
