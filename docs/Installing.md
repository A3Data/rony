# Installing

## Dependencies

- Python (>=3.6)

## Install

```bash
pip install -U rony
```

## Enabling autocompletition (linux users):

For bash:

```bash
echo 'eval "$(_RONY_COMPLETE=source_bash rony)"' >> ~/.bashrc
```

For Zsh:

```bash
echo 'eval "$(_RONY_COMPLETE=source_zsh rony)"' >> ~/.zshrc
```