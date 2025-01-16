[Setup]
AppName={%APPNAME}
AppVersion={%APPVERSION}
WizardStyle=modern
DefaultDirName={commonpf64}\steam\steamapps\common\VA-11 HALL-A
;DefaultGroupName=My Program
;UninstallDisplayIcon={app}\MyProg.exe
Compression=lzma2
SolidCompression=yes

LicenseFile=Lisez-Moi-PatchFR.rtf
;InfoBeforeFile=Readme.rtf
PrivilegesRequired=admin
DisableProgramGroupPage=yes
SetupIconFile=icone.ico
UsePreviousAppDir=yes
LanguageDetectionMethod=none
OutputBaseFilename={%APPNAME}_{%APPVERSION}
Uninstallable=no
CreateUninstallRegKey=no
UpdateUninstallLogAppName=no
UsePreviousLanguage=no

[Files]
Source: "data.win"; DestDir: "{app}"; Flags: ignoreversion
Source: "scripts\eng\*"; DestDir: "{app}\scripts\eng"; Flags: ignoreversion recursesubdirs
Source: "Lisez-Moi-PatchFR.rtf"; DestDir: "{app}"; Flags: isreadme

[Languages]
Name: "fr"; MessagesFile: "compiler:Languages\French.isl"

[Messages]
SelectDirBrowseLabel=Pour continuer, cliquez sur Suivant. Si vous souhaitez choisir un dossier différent, cliquez sur Parcourir.%n %n Veuillez vous assurer que le chemin saisi correspond bien au répertoire de votre jeu. %n En cas de doute, accédez à votre bibliothèque Steam, faites un clic droit sur le jeu, sélectionnez « Gérer » > « Parcourir les fichiers locaux », puis vérifiez que le dossier ouvert correspond bien à celui indiqué ci-dessous.
