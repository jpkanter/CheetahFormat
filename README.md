# Cheetah Format

*Named because it's supposed to be quick and all the other fast-thing-names were gone*

## Usage

`main.py` takes the clipboard content line by line and formats it according to default config.

This thing was cobbled together because I need to extend the Textile code of Redmine a bit but wasn't willing to write the entire text for color and special formats each time anew

## Config 

The formater takes any given string and replaces the enclosed content with the new stuff. 

Typical config

```toml
[Name]
enclosure = "§"
start = "%{color:#0F5D56;font-weight:bold}"
end = "%"
multiline = false
```

This makes it so that `§Richard§` becomes `%{color:#0F5D56;font-weight:bold}Richard%`, basically the same thing that BB-Tags acchived 20 Years ago. It works similar to the normal Markdown Stuff like `**Broad**` becoming **Broad**.

Beware of the kind of tags you use, initially i had `#Date#` which did not work at all because in a long line `#ticketnumber1 bla bla bla #ticketnumber2` got enclosed aswell which is not what i wanted, luckily one can just use `##date##` or something similar (in case of Redmine that still might cause problems as ## is the longtext ticket number variant)

The System isn't perfect but a small help.

### Plans

If I ever find a need or time I might extend this to a small graphical interface to better check on corner cases (stuff like abnormal length detection comes to mind) or a better way to trigger it at all. Maybe even a desktop widget (for KDE then) but I wouldn't depend on it. Its open source, be the change in the world you want.