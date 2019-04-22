# DynDNS  
Einfaches DynDNS Update Skript mit CLI für https://dynv6.com/
 [![Build Status](https://travis-ci.com/ChooseYourPlan/DynDNS.svg?token=be6Muy6Mi7qz4Sp8pyY8&branch=master)](https://travis-ci.com/ChooseYourPlan/DynDNS) [![Build status](https://ci.appveyor.com/api/projects/status/qha8twuxuw8kchs3?svg=true)](https://ci.appveyor.com/project/ChooseYourPlan/dyndns)[![BCH compliance](https://bettercodehub.com/edge/badge/ChooseYourPlan/DynDNS?branch=master)](https://bettercodehub.com/)
 
## Vorbereitung
 
Zur Erstellung eines Hostnames auf https://dynv6.com/ wird ein Benutzerkonto benötigt.

#### Host erstellen 
Nach der Einrichtung eins Benutzerkontos muss einer neuer Host erstellt werden.
Dazu einfach auf den Grünen Button klicken.

![Unbenannt](https://user-images.githubusercontent.com/32968964/56475688-fed34080-648b-11e9-8360-950d380828f4.png)

#### Konfiguration
Als nächstes kommt es zur Konfiguration des Hostes die IPv4 und IPv6 sollten hierbei automatisch ausgefüllt sein.

![Unbenannt](https://user-images.githubusercontent.com/32968964/56475779-79509000-648d-11e9-940b-9808eeccab80.png)

#### Referenzen
Nach der Einrichtung sollte es möglich sein über den Tab **My Hosts -> [Host-Name] (Blau makiert) -> Instructions**
Auf Folgende Seite zu kommen

![Unbenannt](https://user-images.githubusercontent.com/32968964/56476990-8034ce00-64a0-11e9-8c77-7380b21ad94f.png)

Jetzt muss sich folgendes gemerkt werden einmal der **Token** und der eigene **Hostname**. Beide in Rot makiert.

## Windows
Token und Hostname gemerkt geht es weiter mit der Beschaffung des Programms.

Hierzu wahlweise mittels Zip download von:
https://github.com/ChooseYourPlan/DynDNS/archive/master.zip 
oder wenn nur eine Standalone .exe gewünscht ist: 
https://github.com/ChooseYourPlan/DynDNS/raw/master/dist/Updater.exe

Zur Not über den Github Download Button:

![CloneorDownload](https://user-images.githubusercontent.com/32968964/56475415-4952be00-6488-11e9-9fab-82ee9681baf2.png)

Nach dem Download die Kommandzeile über **Windows-Taste+R** und **cmd.exe** öffnen.
Warnung Pfade könnten sich unterscheiden.

Als Erstes Wechseln wir in das richtige Verzeichnis wobei [Benutzer] mit dem Benutzernamen ersetzt werden muss.

```
cd C:\Users\[Benutzer]\Downloads\
```
Powershell wird hier als unzip tool benutzt.
```
powershell Expand-Archive -Force DynDNS-master.zip .DynDNS
```

Die alte Zip Datei wird gelöscht und der Unterordner hervorgeholt.

```
DEL DynDNS-master.zip
move .DynDNS\DynDNS-master DynDNS
```

Wir löschen das alte Verzeichniss und Navigieren zum Windows Standalone Build.

```
RMDIR .DynDNS
cd DynDNS\dist
```

Von hier aus geht es weiter wie als wäre nur die .exe heruntergeladen worden.
Hier kommt wieder der gemerkte Token sowie der Hostname ins Spiel.

Zur Übersicht/Hilfe
```
Updater_winx64.exe -h
```
Die Ausgabe sollte ungefähr wie folgt aussehen:

![image](https://user-images.githubusercontent.com/32968964/56480182-33112600-64b9-11e9-96ca-0a68e12eeccb.png)

Jetzt noch die Angezeigten Parameter mit -u für den Hostnamen und -t für den Token mit übergeben.

```
Updater_winx64.exe -u beispiel-name.dynv6.net -t xxxxxxxxxxxxx-xxxxxxxxxxxxxx-
```
Wenn ein Update erfolgt sollte **addresses updated** ausgeben.
Wenn kein Update erfolgt solle **addresses unchanged** ausgegeben werden.

Alles andere sollte mit dem ausgegebenen Errorn Googlebar sein.  

## Linux
 
In Linux gehen wir den einfachen Weg über das Git Package.

```
sudo apt-get install git -y
```
 
Jetzt noch das Repository klonen mit:
 
```
git clone https://github.com/ChooseYourPlan/DynDNS.git
cd DynDNS
```
 
Entweder wir führen das Python Skript Updater.py aus oder wir Navigieren zum linux build.

```
cd build/exe.linux-x86_64-2.7
``` 
Hier kommt der gemerkte Token sowie der Hostname ins Spiel.

Zur Übersicht/Hilfe
```
./Updater -h
```
Jetzt noch die Angezeigten Parameter mit -u für den Hostnamen und -t für den Token mit übergeben.

```
./Updater -u beispiel-name.dynv6.net -t xxxxxxxxxxxxx-xxxxxxxxxxxxxx-
```
Wenn ein Update erfolgt sollte **addresses updated** ausgeben.
Wenn kein Update erfolgt solle **addresses unchanged** ausgegeben werden.

Alles andere sollte mit dem ausgegebenen Errorn Googlebar sein.  
 
## Abhängikeiten des Builds
 
* [cx_Frezze](https://github.com/anthony-tuininga/cx_Freeze) - Benutzt für den Linux build
* [pyinstaller](https://github.com/pyinstaller/pyinstaller) - Benutzt für den Windows build
* [Requests/Python-Libary](https://github.com/kennethreitz/requests) - Benutzt für HTTP Request im Python Skript
 
## Authors
 
* **Tim Weißenfels** - [ChooseYourPlan](https://github.com/ChooseYourPlan)
 
## License
 
Dieses Projekt ist mit der GPL-3.0 License lizensiert [LICENSE.md](LICENSE.md) 
## Inspiration
 
* https://github.com/ticosax/dynv6-client/blob/master/client.py
