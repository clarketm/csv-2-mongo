# [csv-2-mongo](https://pypi.org/project/csv-2-mongo/)

[![PyPi release](https://img.shields.io/pypi/v/csv-2-mongo.svg)](https://pypi.org/project/csv-2-mongo/)
[![Downloads](https://pepy.tech/badge/csv-2-mongo)](https://pepy.tech/project/csv-2-mongo)

Import a CSV to MongoDB using Python 🐍.

## Installation

```bash
$ pip install csv-2-mongo
```

## Usage

```text

Usage: csv_2_mongo.py [OPTIONS] FILE

  Import a csv FILE to MongoDB

Options:
  -h, --help             Show this message and exit.
  -v, --version          Show the version and exit.
  -d, --database name    Database name.  [default: test]
  -c, --collection name  Collection name.  [default: test]
  -H, --host host        Host name.  [default: 0.0.0.0]
  -p, --port port        Port number.  [default: 27017]
  -t, --timeout sec      Connection timeout (seconds).  [default: 5]
  -f, --force            Overwrite collection if exists.
  -y, --yes              Automatic yes to prompts.

```

> Note: CSV headers are **required** to correctly correlate MongoDB `fields` to CSV `fields`. 

## Examples

Import `mammals.csv` to a `mammals` collection in the  `animals` database:

```bash
$ csv-2-mongo -d animals -c mammals ./mammals.csv
```

```txt
....................................
Connecting to 0.0.0.0:27017
....................................

Import data.csv to database=animals collection=mammals [y/N]? y
Import complete!
```

Import `mammals.csv` to a `mammals` collection in the  `animals` database **overwriting the collection if it exists**:

> Note: the `-f, --force` flag will overwrite the collection without a prompt. If the flag is omitted, `csv-2-mongo` will prompt you before operations with potential data loss.

```bash
$ csv-2-mongo -f -d animals -c mammals ./mammals.csv
```

```txt
....................................
Connecting to 0.0.0.0:27017
....................................

Import data.csv to database=animals collection=mammals [y/N]? y
Import complete!
```

Import `mammals.csv` to a `mammals` collection in the  `animals` database running on *host* **mongo.travismclarke.com** at *port* **27111**:

```bash
$ csv-2-mongo -d animals -c mammals -H mongo.travismclarke.com -p 27111 ./mammals.csv
```

```txt
....................................
Connecting to mongo.travismclarke.com:27111
....................................

Import data.csv to database=animals collection=mammals [y/N]? y
Import complete!
```

To skip the prompt (e.g. `Import data.csv to ...`), such as running via a script, one can pass the `-y`, `--yes` flag to force a *yes* response to the confirmation prompt:

> Note: this will not suppress the *overwrite* prompt which still requires the `-f, --force` flag.

```bash
$ csv-2-mongo -y -d animals -c mammals ./mammals.csv
```

```txt
....................................
Connecting to 0.0.0.0:27017
....................................

Import complete!
```


## License

MIT &copy; [**Travis Clarke**](https://blog.travismclarke.com/)
