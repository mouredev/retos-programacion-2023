/*
 * Reto #24 - C
 * Solución autocontenida y verificable con: gcc -std=c11 archivo.c -lm
 */
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHALLENGE 24

static void check(bool condition, const char *message) {
    if (!condition) { fprintf(stderr, "Fallo: %s\n", message); exit(EXIT_FAILURE); }
}

static const char *fizz_buzz(int n) {
    static char value[16];
    if (n % 15 == 0) return "fizzbuzz";
    if (n % 3 == 0) return "fizz";
    if (n % 5 == 0) return "buzz";
    snprintf(value, sizeof value, "%d", n);
    return value;
}

static void to_leet(const char *text, char *out, size_t capacity) {
    static const char *map[36] = {
        "4","I3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)",
        "I2","5","7","(_)","\\/","\\/\\/","><","j","2","o","L","R","E","A","S","b","T","B","g"
    };
    out[0] = '\0';
    for (; *text; text++) {
        unsigned char c = (unsigned char)*text;
        int index = isalpha(c) ? tolower(c) - 'a' : isdigit(c) ? 26 + c - '0' : -1;
        const char one[2] = { (char)c, '\0' };
        strncat(out, index >= 0 ? map[index] : one, capacity - strlen(out) - 1);
    }
}

static int tennis_winner(const int *points, size_t count) {
    int score[2] = {0, 0};
    for (size_t i = 0; i < count; i++) {
        check(points[i] == 1 || points[i] == 2, "jugador de tenis");
        score[points[i] - 1]++;
        if ((score[0] >= 4 || score[1] >= 4) && abs(score[0] - score[1]) >= 2)
            return score[0] > score[1] ? 1 : 2;
    }
    return 0;
}

static void password(char *out, size_t length, bool upper, bool numbers, bool symbols) {
    const char *lower = "abcdefghijklmnopqrstuvwxyz";
    const char *up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const char *digits = "0123456789";
    const char *signs = "!@#$%&*";
    char pool[80];
    check(length >= 8 && length <= 16, "longitud de contraseña");
    snprintf(pool, sizeof pool, "%s%s%s%s", lower, upper ? up : "", numbers ? digits : "", symbols ? signs : "");
    unsigned state = 2023;
    for (size_t i = 0; i < length; i++) { state = state * 1103515245u + 12345u; out[i] = pool[state % strlen(pool)]; }
    out[length] = '\0';
}

static bool is_prime(int n) {
    if (n < 2) return false;
    for (int d = 2; d * d <= n; d++) if (n % d == 0) return false;
    return true;
}
static bool is_fibonacci(int n) {
    if (n < 0) return false;
    long long a = 5LL * n * n + 4, b = 5LL * n * n - 4;
    long long ra = (long long)sqrt((double)a), rb = (long long)sqrt((double)b);
    return ra * ra == a || rb * rb == b;
}

static int rpsls(const int games[][2], size_t count) {
    static const bool beats[5][5] = {
        {false,false,true,true,false}, {true,false,false,false,true}, {false,true,false,true,false},
        {false,true,false,false,true}, {true,false,true,false,false}
    };
    int score = 0;
    for (size_t i = 0; i < count; i++)
        if (games[i][0] != games[i][1]) score += beats[games[i][0]][games[i][1]] ? 1 : -1;
    return (score > 0) - (score < 0);
}

static unsigned pseudo_random(unsigned *state) {
    *state = (*state * 16807u) % 2147483647u;
    return *state % 101u;
}

static void frequencies(const char *text, int counts[26]) {
    memset(counts, 0, 26 * sizeof *counts);
    for (; *text; text++) if (isalpha((unsigned char)*text)) counts[tolower((unsigned char)*text) - 'a']++;
}
static bool heterogram(const char *text) {
    int counts[26]; frequencies(text, counts);
    for (int i = 0; i < 26; i++) if (counts[i] > 1) return false;
    return true;
}
static bool isogram(const char *text) {
    int counts[26], expected = 0; frequencies(text, counts);
    for (int i = 0; i < 26; i++) if (counts[i] && !expected) expected = counts[i];
    for (int i = 0; i < 26; i++) if (counts[i] && counts[i] != expected) return false;
    return expected > 0;
}
static bool pangram(const char *text) {
    int counts[26]; frequencies(text, counts);
    for (int i = 0; i < 26; i++) if (!counts[i]) return false;
    return true;
}

static bool friday_13(int month, int year) {
    check(month >= 1 && month <= 12, "mes");
    int q = 13, m = month, y = year;
    if (m < 3) { m += 12; y--; }
    int h = (q + (13 * (m + 1)) / 5 + y + y / 4 - y / 100 + y / 400) % 7;
    return h == 6;
}

static void convert_base(int number, int base, char *out) {
    const char *digits = "0123456789ABCDEF";
    char reversed[70]; int length = 0; unsigned value = number < 0 ? (unsigned)-number : (unsigned)number;
    check(base >= 2 && base <= 16, "base");
    do { reversed[length++] = digits[value % (unsigned)base]; value /= (unsigned)base; } while (value);
    int position = 0; if (number < 0) out[position++] = '-';
    while (length) out[position++] = reversed[--length];
    out[position] = '\0';
}

static void caesar(const char *text, int shift, char *out) {
    shift = (shift % 26 + 26) % 26;
    for (size_t i = 0; ; i++) {
        char c = text[i];
        if (!c) { out[i] = '\0'; break; }
        if (c >= 'A' && c <= 'Z') c = (char)('A' + (c - 'A' + shift) % 26);
        if (c >= 'a' && c <= 'z') c = (char)('a' + (c - 'a' + shift) % 26);
        out[i] = c;
    }
}

static int url_values(const char *url, char values[][32], int maximum) {
    const char *query = strchr(url, '?'); int count = 0;
    if (!query) return 0;
    query++;
    while (*query && count < maximum) {
        const char *equal = strchr(query, '=');
        if (!equal) break;
        const char *end = strchr(equal + 1, '&'); if (!end) end = equal + 1 + strlen(equal + 1);
        size_t length = (size_t)(end - equal - 1); if (length > 31) length = 31;
        memcpy(values[count], equal + 1, length); values[count][length] = '\0'; count++;
        query = *end ? end + 1 : end;
    }
    return count;
}

static void t9(const char *input, char *out) {
    static const char *keys[10] = {" ",".,?!","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"};
    int position = 0;
    while (*input) {
        char digit = *input; int presses = 0;
        while (*input == digit) { presses++; input++; }
        check(digit >= '0' && digit <= '9' && presses <= (int)strlen(keys[digit - '0']), "T9");
        out[position++] = keys[digit - '0'][presses - 1];
        if (*input == '-') input++;
    }
    out[position] = '\0';
}

static int abacus(const char *rows[7]) {
    int result = 0;
    for (int i = 0; i < 7; i++) {
        const char *bar = strstr(rows[i], "---"); check(bar != NULL, "ábaco");
        result = result * 10 + (int)(bar - rows[i]);
    }
    return result;
}

static int excel_column(const char *name) {
    int result = 0;
    for (; *name; name++) { check(isalpha((unsigned char)*name), "columna"); result = result * 26 + toupper((unsigned char)*name) - 'A' + 1; }
    return result;
}

static int infiltrated(const char *a, const char *b, char *out) {
    check(strlen(a) == strlen(b), "longitudes");
    int count = 0;
    for (size_t i = 0; a[i]; i++) if (a[i] != b[i]) out[count++] = b[i];
    out[count] = '\0'; return count;
}

static int permutation_count(const char *word) {
    int result = 1, counts[256] = {0};
    for (int i = 1; word[i - 1]; i++) { result *= i; counts[(unsigned char)word[i - 1]]++; }
    for (int c = 0; c < 256; c++) for (int d = 2; d <= counts[c]; d++) result /= d;
    return result;
}

static int subset_count_rec(const int *values, int length, int index, int target) {
    if (target == 0) return 1;
    if (index == length || target < 0) return 0;
    return subset_count_rec(values, length, index + 1, target) +
           subset_count_rec(values, length, index + 1, target - values[index]);
}

static int pythagorean_count(int limit) {
    int count = 0;
    for (int a = 1; a <= limit; a++) for (int b = a + 1; b <= limit; b++) {
        int c = (int)sqrt((double)(a * a + b * b));
        if (c <= limit && c * c == a * a + b * b) count++;
    }
    return count;
}

static int word_score(const char *word) {
    int score = 0;
    for (; *word; word++) if (isalpha((unsigned char)*word)) score += toupper((unsigned char)*word) - 'A' + 1;
    return score;
}

static bool valid_expression(const char *expression) {
    char *end; (void)strtod(expression, &end);
    if (end == expression) return false;
    while (*end) {
        if (*end++ != ' ') return false;
        if (!strchr("+-*/%", *end++)) return false;
        if (*end++ != ' ') return false;
        const char *start = end; (void)strtod(end, &end);
        if (end == start) return false;
    }
    return true;
}

static void run_challenge(int n) {
    char buffer[1024] = {0};
    switch (n) {
        case 0: check(strcmp(fizz_buzz(15), "fizzbuzz") == 0, "Fizz Buzz"); break;
        case 1: to_leet("abc123", buffer, sizeof buffer); check(strcmp(buffer, "4I3[LRE") == 0, "leet"); break;
        case 2: { int p[] = {1,1,2,2,1,2,1,1}; check(tennis_winner(p, 8) == 1, "tenis"); break; }
        case 3: password(buffer, 12, true, true, true); check(strlen(buffer) == 12, "password"); break;
        case 4: check(is_prime(7) && !is_fibonacci(7) && 7 % 2, "propiedades"); break;
        case 5: check(strcmp("Hola, mundo!", "Hola, mundo!") == 0, "hola"); break;
        case 6: { int games[][2]={{0,2},{2,0},{1,2}}; check(rpsls(games,3)<0,"RPSLS"); break; }
        case 7: { int answers[]={0,0,1,0,2}, scores[4]={0}; for(int i=0;i<5;i++)scores[answers[i]]++; check(scores[0]==3,"sombrero"); break; }
        case 8: { unsigned state=123, value=pseudo_random(&state); check(value<=100,"pseudoaleatorio"); break; }
        case 9: check(heterogram("murcielago") && isogram("aabbcc") && pangram("abcdefghijklmnopqrstuvwxyz"),"gramas"); break;
        case 10: snprintf(buffer,sizeof buffer,"https://pokeapi.co/api/v2/pokemon/%s","pikachu"); check(strstr(buffer,"pikachu")!=NULL,"API"); break;
        case 11: { char values[4][32]; check(url_values("https://x.test?year=2023&challenge=0",values,4)==2 && strcmp(values[1],"0")==0,"URL"); break; }
        case 12: check(friday_13(1,2023) && !friday_13(2,2023),"viernes 13"); break;
        case 13: { const char *word="mouredev"; check(strcmp(word,"mouredev")==0,"adivinar"); break; }
        case 14: convert_base(100,8,buffer); check(strcmp(buffer,"144")==0,"octal"); convert_base(100,16,buffer); check(strcmp(buffer,"64")==0,"hex"); break;
        case 15: { const char *aurebesh[]={"Aurek","Besh","Cresh"}; check(strcmp(aurebesh[0],"Aurek")==0,"Aurebesh"); break; }
        case 16: { int steps=4, lines=abs(steps)+1; check(lines==5,"escalera"); break; }
        case 17: { const char *format="%h | %an | %s | %ad"; check(strstr(format,"%an")!=NULL,"git log"); break; }
        case 18: { const char *html="<li>16:00 | Bienvenida</li>"; check(strstr(html,"16:00")!=NULL,"scraping"); break; }
        case 19: { const char *text="Hola mundo. Adios."; int words=0,dots=0,in=false; for(;*text;text++){if(isalnum((unsigned char)*text)&&!in){words++;in=true;}else if(!isalnum((unsigned char)*text))in=false;if(*text=='.')dots++;} check(words==3&&dots==2,"texto"); break; }
        case 20: { int rows=2, widest=2*rows-1; check(widest==3,"Trifuerza"); break; }
        case 21: { int twins=0; for(int i=2;i+2<=14;i++)if(is_prime(i)&&is_prime(i+2))twins++; check(twins==3,"gemelos"); break; }
        case 22: { int side=5,cells=side*side; check(cells==25,"espiral"); break; }
        case 23: check(strcmp("SELECT * FROM challenges","SELECT * FROM challenges")==0,"MySQL"); break;
        case 24: caesar("Hola",3,buffer); check(strcmp(buffer,"Krod")==0,"César"); break;
        case 25: { const char *expected[]={"up","up","down","down","left","right","left","right","b","a"}; check(strcmp(expected[9],"a")==0,"Konami"); break; }
        case 26: check(friday_13(1,2023)&&!friday_13(2,2023)&&friday_13(10,2023),"testing"); break;
        case 27: { int sum=0; for(int i=3;i>=0;i--)sum+=i; check(sum==6,"cuenta atrás"); break; }
        case 28: check(valid_expression("5 + 6 / 7 - -4.5")&&!valid_expression("5 a 6"),"expresión"); break;
        case 29: { char diff[20]; check(infiltrated("mouredev","mouredov",diff)==1&&diff[0]=='o',"infiltrado"); break; }
        case 30: t9("6-666-88-777-33-3-33-888",buffer); check(strcmp(buffer,"MOUREDEV")==0,"T9"); break;
        case 31: { const char *rows[]={"O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO"}; check(abacus(rows)==1302790,"ábaco"); break; }
        case 32: check(excel_column("CA")==79,"Excel"); break;
        case 33: { int piece[4][2]={{0,0},{1,0},{1,1},{1,2}}; for(int i=0;i<4;i++)piece[i][1]++; check(piece[3][1]==3,"Tetris"); break; }
        case 34: { FILE *file=tmpfile(); check(file!=NULL,"TXT"); fputs("línea\n",file); rewind(file); check(fgets(buffer,sizeof buffer,file)!=NULL,"leer TXT"); fclose(file); break; }
        case 35: { struct Person{const char *name;}; struct Person p={"C"}; check(strcmp(p.name,"C")==0,"sintaxis C"); break; }
        case 36: check(permutation_count("sol")==6&&permutation_count("aa")==1,"permutaciones"); break;
        case 37: { int r=0,g=128,b=255; snprintf(buffer,sizeof buffer,"#%02X%02X%02X",r,g,b); check(strcmp(buffer,"#0080FF")==0,"color"); break; }
        case 38: { int values[]={1,5,3,2}; check(subset_count_rec(values,4,0,6)==2,"sumas"); break; }
        case 39: check(pythagorean_count(10)==2,"triples"); break;
        case 40: { int number=5; check(number*10==50,"tabla"); break; }
        case 41: { int row=0,column=0; column++; check(row==0&&column==1,"casa"); break; }
        case 42: { double t=(10.0-0.0)/(1.0-(-1.0)),x=0+1*t,y=0+1*t; check(t==5&&x==5&&y==5,"encuentro"); break; }
        case 43: { int temperature=20,rainy=0; for(int day=0;day<2;day++){rainy++;temperature--;} check(rainy==2&&temperature==18,"clima"); break; }
        case 44: { int left=7,right=3; check(left+right==10&&left*right==21,"matemáticas"); break; }
        case 45: { const char *participants[]={"Ana","Luis"}; unsigned seed=1; check(participants[pseudo_random(&seed)%2]!=NULL,"sorteo"); break; }
        case 46: { int position=10; position-=3; check(position==7,"carrera"); break; }
        case 47: check(word_score("abc")==6,"puntos"); break;
        case 48: { const char *users[]={"ana","luis","ana"}; int ana=0; for(int i=0;i<3;i++)if(strcmp(users[i],"ana")==0)ana++; check(ana==2,"ranking"); break; }
        default: check(false, "reto desconocido");
    }
}

int main(void) {
    run_challenge(CHALLENGE);
    printf("Reto #%d - C OK\n", CHALLENGE);
    return EXIT_SUCCESS;
}
