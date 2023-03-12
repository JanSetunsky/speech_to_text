$DefaultPath = $PSScriptRoot
chcp 1250
$SpeechData  = python "$DefaultPath\speech_process.py" --encoding utf-8

[string]$SpeechText  = ($SpeechData | select -Last 1 | ConvertFrom-Json ).Text

Set-Clipboard -Value $SpeechText

