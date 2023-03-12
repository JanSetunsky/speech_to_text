# speech_to_text

Converts speech using a microphone into text form, which returns the output to the clipboard.
It was developed for use by [chat.openai]{https://chat.openai.com/}

## Requirements

You need to have PowerShell and Python with the following libraries installed to run successfully.
`pip install threading`
`pip install pyaudio`
`pip install SpeechRecognition`
`pip install Keyboard`

## Startup process

Run the `speech_to_text.bat` file which activates the microphone in Windows and you can speak immediately.
Press ESC to stop recording.
In a short time, the speech recognition process is completed and the content of the speech, converted to text, is automatically in your clipboard. You can then immediately paste it into the text area in your session [chat.openai]{https://chat.openai.com/}
This speeds up the process of communicating with AI and you don't have to pay flat fees.

## Settings

By default, the language `cs-CZ` is set, but you can change it to another.

The decoding is set to utf-8 and then the decoding changes to chcp 1250.

If you are using a language package other than English or Czech, you will have to modify the decoding so that the resulting text meets your requirements.

## Shortcut

There is a `speech_to_text.lnk` file in the package that uses the `explorer.exe` process to invoke the `.bat` file.
Open the file properties and in the `target` line create the target path to run the `.bat` batch file.

For example:
`C:\Windows\explorer.exe "d:\github\speech_to_text\speech_to_text.bat"`
It is convenient to place this icon on the Windows taskbar, and then you can easily start the speech-to-text service and use it as a shortcut.