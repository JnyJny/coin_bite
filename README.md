# Purpose

This repo shows a couple of different ways to implement a prospective bite
and then test each of those implementations with the same pytest test. 


## Testing

Clone this repo and change directory into the repo:

```console
$ git clone https://github.com/JnyJny/coin_bite
$ cd coin_bite
```

### With Poetry

```console
$ poetry run poe test
```

### With VirtualEnv
```
$ py -m venv venv
$ source venv/bin/activate
<venv> $ py -m pip install -r requirements.txt
<venv> $ poe test
```


