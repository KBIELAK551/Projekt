# Projekt
SYMULACJA ROZPRZESTRZENIANIA SIĘ CHOROBY ZAKAŹNEJ

"Symulacja rozprzestrzeniania się choroby zakaźnej na przykładzie poruszających się kul w ograniczonej przestrzeni dwuwymiarowej. W stanie początkowym tylko jedna z N kul jest nosicielem choroby.

Następnie kule zaczynają poruszać, zgodnie z losowym wektorem prędkości początkowej. W momencie gdy kula zarażona zderzy się z kulą niezarażoną, następuje transmisja choroby. Zderzenia kul oraz kuli ze ścianą ograniczającą przestrzeń są elastyczne, obowiązują prawa fizyki. Każda z zarażonych kul może zarażać tylko przez określony czas T, po czym przechodzi w stan, w którym jest chora, ale nie zaraża innych. Ponadto, część kul jest nieruchoma (jest to parametr wejściowy programu).

Należy zwizualizować proces ruchu kul oraz wykres liczby kul zdrowych oraz zarażonych (z podziałem na te, które są w stanie zarażać innych i te, które były chore przez dłużej niż T)."

# Włączenie gry 
Symulacja jest przedstawiona w oknie pygame. By móc uruchomić symulację należy zainstalować pygame oraz uruchomić plik "Projekt_Kacper_Bielak". W terminalu program bedzie prosić o "Enter the number of balls" czyli o podanie ilości kul która ma się pojawić w symulacji, następnie "Enter the time of epidemic transmission:" tutaj zatem należy podać czas rozprzestrzeniania się choroby, na końcu "enter the number of stationary balls:" tutaj zatem należy podać ilość kul nieruchomych, po wpisaniu wartości Program uruchomi się a na ekranie pojawi się okno z symulacją:
# Opis powstania projektu
Projekt na początku miał powstać na zasadzie gry "Plague.inc", lecz forma oraz wielkość projektu znacznie przewyższyła moje umiejętności oraz czas. Postanowiłem na wykonanie symulacji na własną rękę. Nauka o pygame oraz umiejętności zdobyte podczas zajęć pomogły mi znacząco. Na początku utworzenie okna w którym będą się poruszać kule. następnie forma odbijania czyli prawa fizyki które wydawały się najtrudniejszym krokiem, lecz okazało się że są jednym z łatwiejszych. Logika odbicia od ścian zależy od pozycji kuli(z uwzględnieniem promienia) jest większa niz pozycja ścian to wektor ruchu kuli musi być odwrócony o 180 stopni. Następnie pobranie danych wejściowych, liczby kul oraz czasu transmisji choroby.






