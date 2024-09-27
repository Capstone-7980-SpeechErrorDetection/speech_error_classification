# Sound Event Detection for Speech Error Detection

To run the code, you need to install the following libraries:

- python=3.10
- numpy<2
- librosa
- soxr
- scipy
- soundfile
- audioread
- pandas
- tensorflow
- keras

Save the audio files (.wav) in the `data/audio` folder.

The dataset (.csv) should be saved in the `data/metadata` folder. The dataset should have the following columns:

- `file`: the name of the audio file
- `label`: the label of the speech error
- `start`: the start time of the speech error
- `end`: the end time of the speech error

The WhisperX transcript files (.csv) should be saved in the `data/whisperX` folder. The transcript files should have the following columns:

- `start`: the start time of a speech segment
- `end`: the end time of a speech segment
- `text`: the text of the speech segment

To run the training, you need to run the following command:

`bash scripts/pipeline.sh`
this is owned by Bo
