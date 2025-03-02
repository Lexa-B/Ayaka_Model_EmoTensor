import sys
import os
from datetime import datetime
import base32_crockford

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ayaka_models_emotensor.EmoTensorModels import EmoTensorFull_CTXD, EmoTensor4DSlice_CTXD, EmoTensor3DSlice_CTXD, EmoTensor2DSlice_CTXD, EmoTensor1DSlice_CTXD

ThisTransient = EmoTensor4DSlice_CTXD(
    timestamp=datetime.now().isoformat(),
    message="こんにちは！",
    speaker_user="uid=1",
    emotional_context="アシスタント is greeting 花子, ready to assist her with her needs.",
    emoters=[
        EmoTensor3DSlice_CTXD(
            emoter_user="uid=1",
            external_context="アシスタント is sending this message to 花子 via LINE.",
            targets=[
                EmoTensor2DSlice_CTXD(
                    this_target="uid=1-uid=5",
                    scratch_context="アシスタント is sending this message to 花子 via LINE.",
                    scratch_synopsis="アシスタント is sending this message to 花子 via LINE.",
                    emotions=[
                        EmoTensor1DSlice_CTXD(
                            emotion="Joy",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Trust",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Fear",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Surprise",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Sadness",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Disgust",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Anger",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Anticipation",
                            context="アシスタント is sending this message to 花子 via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        )
                    ]
                ),
                EmoTensor2DSlice_CTXD(
                    this_target="uid=5-uid=1",
                    scratch_context="花子 is receiving a greeting from アシスタント via LINE.",
                    scratch_synopsis="花子 is receiving a greeting from アシスタント via LINE.",
                    emotions=[
                        EmoTensor1DSlice_CTXD(
                            emotion="Joy",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Trust",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Fear",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Surprise",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Sadness",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Disgust",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Anger",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        ),
                        EmoTensor1DSlice_CTXD(
                            emotion="Anticipation",
                            context="花子 is receiving a greeting from アシスタント via LINE.",
                            intensity=0.0,
                            valence=0.0,
                            arousal=0.0
                        )
                    ]
                )
            ]
        )
    ]
)
with open("TEST-EmoTensor.etsc", "r") as f:
    EmoTensor = EmoTensorFull_CTXD.model_validate_json(f.read())
    # Add the transient to the EmoTensor
    EmoTensor.transients.append(ThisTransient)

    # Add the transient ID to the EmoTensor order_5_transients list
    if len(EmoTensor.order_5_transients) == 0:
        next_transient = "c_0_0_0" # If there are no transients, start at 0
    else:
        last_transient = EmoTensor.order_5_transients[-1]
        last_segment = last_transient.split('_')[-1]
        try:
            last_number = base32_crockford.decode(last_segment)
            next_number = last_number + 1
            next_transient = f"c_0_0_{base32_crockford.encode(next_number)}"
        except ValueError:
            # If we can't decode the last segment, start a new sequence
            next_transient = "c_0_0_0"
    EmoTensor.order_5_transients.append(next_transient)

with open("TEST-EmoTensor.etsc", "w") as f:
    f.write(EmoTensor.model_dump_json(indent=2))