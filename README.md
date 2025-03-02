# Ayaka Model EmoTensor

Emotion Tensor Models for Ayaka

## Installation

You can install this package directly from GitHub using pip:

```bash
pip install git+https://github.com/Lexa-B/Ayaka_Model_EmoTensor.git
```

## Usage

```bash
# Initialize the sliced contextualized tensor
python3 tests/TEST-TensorInit_SlicedContextualized.py

# Generate a sample transient
python3 tests/TEST-TransientGen.py
```
*If you need an EmoDescFile (if you're running this standalone), then an example can be obtained from https://github.com/Lexa-B/Ayaka_MS_EmoTensorGen/blob/main/Configs/EmoList_Plutchik.xml*

If all goes well, you should see a new file called `TEST-EmoTensor.etsc` in your directory.
It should look like this:

```json
{
  "version": "v0.0.2-EmoTensor Sliced Contextualized",
  "order_1_attributes": [
    "Intensity",
    "Valence",
    "Arousal",
    "Context"
  ],
  "order_2_emotions": [
    "Intensity",
    "Valence",
    "Arousal",
    "Context"
  ],
  "order_3_target": [
    "uid=1-uid=5",
    "uid=5-uid=1"
  ],
  "order_4_emoters": [
    "uid=1",
    "uid=5"
  ],
  "order_5_transients": [
    "c_0_0_0+2025-03-02T14:54:40.951390"
  ],
  "user_prefnames": [
    "アシスタント",
    "花子"
  ],
  "transients": [
    {
      "timestamp": "2025-03-02T14:54:40.950994",
      "message": "こんにちは！",
      "speaker_user": "uid=1",
      "emotional_context": "アシスタント is greeting 花子, ready to assist her with her needs.",
      "emoters": [
        {
          "emoter_user": "uid=1",
          "external_context": "アシスタント is sending this message to 花子 via LINE.",
          "targets": [
            {
              "this_target": "uid=1-uid=5",
              "scratch_context": "アシスタント is sending this message to 花子 via LINE.",
              "scratch_synopsis": "アシスタント is sending this message to 花子 via LINE.",
              "emotions": [
                {
                  "emotion": "Joy",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Trust",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Fear",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Surprise",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Sadness",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Disgust",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Anger",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Anticipation",
                  "context": "アシスタント is sending this message to 花子 via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                }
              ]
            },
            {
              "this_target": "uid=5-uid=1",
              "scratch_context": "花子 is receiving a greeting from アシスタント via LINE.",
              "scratch_synopsis": "花子 is receiving a greeting from アシスタント via LINE.",
              "emotions": [
                {
                  "emotion": "Joy",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Trust",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Fear",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Surprise",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Sadness",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Disgust",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Anger",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                },
                {
                  "emotion": "Anticipation",
                  "context": "花子 is receiving a greeting from アシスタント via LINE.",
                  "intensity": 0.0,
                  "valence": 0.0,
                  "arousal": 0.0
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```



## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License - see the [LICENSE](LICENSE) file for details.
