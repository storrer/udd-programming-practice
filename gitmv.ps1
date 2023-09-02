# Get the current directory
$currentDirectory = Get-Location

# Get all .py files in the current directory
$pyFiles = Get-ChildItem -Path $currentDirectory -Filter "*.py"

# Loop through each .py file
foreach ($pyFile in $pyFiles) {

    # Get the original filename
    $originalFilename = $pyFile.Name

    # Replace hyphens with underscores
    $newFilename = $originalFilename -replace "-", "_"

    # Rename the file using git mv
    git mv $originalFilename $newFilename
}