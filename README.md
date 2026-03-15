# Copyright Infringement Detector

This project was made in an effort to explore the issue of small arts businesses' content being stolen and reuploaded as a cheaper product on other third party sites.

## Planned file structure

```
copyright_infringement_detection/
├─ src/                         # TypeScript app code
│  ├─ index.ts                  # main pipeline
│  ├─ scrapers/
│  ├─ parsers/
│  └─ types/
├─ ml/                          # Python ML code
│  ├─ preprocessing/            # cleaning/feature building
│  ├─ training/                 # model training
│  ├─ inference/                # load model + generate predictions
│  ├─ evaluation/               # determine accuracy, precision, recall, F1
├─ data/                        # shared inputs/outputs
└─ models/
```

## To start
1. `cd src`
2. `npm install`
3. `npm run dev`
