# Telegram Profile Updater

## By default, for the program, I update the time in my bio profile every minute, and a random emoji is placed at the end of the text every time.

<hr>

### In order for the bot to work, you need to define the API_ID and API_HASH variables of your Telegram account.

<hr>

### You can set your text on your first name and last name, except for the profile bio, and just change the argument in the update_profile function:

<br>

### For biography(default):

<br>

```python
app.update_profile(bio=text)
```

<br>

### For first name:

<br>

```python
app.update_profile(first_name=text)
```

<br>

### For last name:

<br>

```python
app.update_profile(last_name=text)
```

<hr>

**This project is mostly fun :)**
