$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$cli = Join-Path $scriptDir "slackbox_cli.py"

$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) {
    & $py.Source -3 $cli init @args
    exit $LASTEXITCODE
}

$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    & $python.Source $cli init @args
    exit $LASTEXITCODE
}

Write-Error "Slackbox setup requires Python 3. Install Python 3 and try again."
exit 127
