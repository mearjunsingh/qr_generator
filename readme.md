# Bulk QR File Generator

app -> data -> filename.py

Samples:
```python
DIFF_LABELED_QR_DATA = [
    {"label": "A10-1", "qrc": "e5:9KYOD:gO5GyWC2fX3PoFTAZQcgQw=="},
]
```
```python
SAME_LABELED_QR_DATA = {
    "A10": [
        "e5:9KYOD:gO5GyWC2fX3PoFTAZQcgQw==",
        "e5:9KYOD:SUyIjvBXnfxkR6ic7ILZ7A==",
    ]
}
```
```python
QR_DATA = [
    "e5:LE5ME:HyKy2Tv8SvAJ77ICpx8zYg==",
]
```

import filename and send in template from views
