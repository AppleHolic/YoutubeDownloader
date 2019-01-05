### Simple Youtube Downloader

- It download youtube video from given urls

#### Setup

- Install python packages and ffmpeg (MacOS)
 
```
$$ sh setup.sh
```

- Download folder
  - see configs.py YDL_MASTER_PATH

#### Functions

1. from_file

- file sample
  - url, filename lines (there is no blank lines between urls)

>
> url1 filename1 
>
> url2 filename2
>
> ...

- command sample

```bash
$$ python run.py from_file samples/target.txt
```
