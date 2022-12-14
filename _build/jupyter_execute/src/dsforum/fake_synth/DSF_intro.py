#!/usr/bin/env python
# coding: utf-8

# # Intro Data Science Forum - Fake & Synthetic Data
# 
# ## Data Masking (Data Maskering)
# 
# 
# Gitt de økende cybertruslene og implementeringen av personvernlovgivning som GDPR i EU eller CCPA i USA, må bedrifter sørge for at private data brukes så lite som mulig. Datamaskering gir en måte å begrense private data på, samtidig som det lar bedrifter teste systemene sine med data så nærme reelle data som mulig.
# 
# Den gjennomsnittlige kostnaden for et datainnbrudd ble estimert til 4,24 millioner dollar i 2020, noe som skaper sterke insentiver for bedrifter til å investere i informasjonssikkerhetsløsninger, inkludert datamaskering for å beskytte sensitive data. Datamaskering er en må-ha-løsning for organisasjoner som ønsker å overholde GDPR eller bruke realistiske data i et testmiljø.
# 
# I denne artikkelen forklarer vi datamaskering og gir en liste over de beste datamaskeringsteknikkene.
# 
# Hva er datamaskering?
# Datamaskering blir også referert til som dataobfuskering, dataanonymisering eller pseudonymisering. Det er prosessen med å erstatte konfidensielle data ved å bruke funksjonelle fiktive data som tegn eller andre data. Hovedformålet med datamaskering er å beskytte sensitiv, privat informasjon i situasjoner der virksomheten deler data med tredjeparter.
# 
# Hvorfor er datamaskering viktig nå?
# Antallet datainnbrudd øker hvert år (Sammenlignet med midten av 2018, var antallet registrerte brudd opp 54 % i 2019) Derfor må organisasjoner forbedre sine datasikkerhetssystemer. Behovet for datamaskering øker på grunn av følgende årsaker:
# 
# Organisasjoner trenger en kopi av produksjonsdata når de bestemmer seg for å bruke dem for ikke-produksjonsmessige årsaker, for eksempel applikasjonstesting eller forretningsanalysemodellering.
# Foretakets retningslinjer for personvern er også truet av innsidere. Derfor bør organisasjoner fortsatt være forsiktige mens de gir tilgang til innsidemedarbeidere.
# GDPR og CCPA tvinger bedrifter til å styrke databeskyttelsessystemene sine, ellers må organisasjoner betale høye bøter.
# Hvordan fungerer datamaskering?
# Datamaskeringsprosessen er enkel, men den har forskjellige teknikker og typer. Generelt begynner organisasjoner med å identifisere alle sensitive data bedriften din har. Deretter bruker de algoritmer for å maskere sensitive data og erstatte dem med strukturelt identiske, men numerisk forskjellige data. Hva mener vi med strukturelt identiske? For eksempel er passnumre 9 sifre i USA, og enkeltpersoner må vanligvis dele passinformasjonen sin med flyselskaper. Når et flyselskap bygger en modell for å analysere og teste forretningsmiljøet, oppretter de en annen 9-sifret lang pass-ID eller erstatter noen sifre med tegn.
# 
# Her er et eksempel på hvordan datamaskering fungerer:
# 
# <img src="https://research.aimultiple.com/wp-content/uploads/2020/07/Data-masking-example-2.png" alt="Informatica">
# Hva er teknikkene for datamaskering?
# Det er mange datamaskeringsteknikker. Her gir vi 8 teknikker som vi klassifiserte i henhold til deres brukstilfelle.
# 
# Egnet for testdatahåndtering
# Substitusjon
# I substitusjonstilnærmingen, som navnet refererer til, erstatter virksomheter de originale dataene med tilfeldige data fra levert eller tilpasset oppslagsfil. Dette er en effektiv måte å skjule data på siden bedrifter bevarer det autentiske utseendet til data.
# 
# Blander
# Blanding er en annen vanlig datamaskeringsmetode. I stokkingsmetoden, akkurat som substitusjon, erstatter bedrifter originaldata med andre data som ser autentisk ut, men de blander enhetene i samme kolonne tilfeldig.
# 
# Antall og datoavvik
# For økonomiske og datodrevne datasett endres ikke nøyaktigheten til datasettet når du bruker samme varians for å opprette et nytt datasett mens data maskeres. Å bruke varians for å lage et nytt datasett er også ofte brukt i syntetisk datagenerering. Hvis du planlegger å beskytte personvernet med denne teknikken, anbefaler vi deg å lese vår omfattende veiledning for generering av syntetiske data.
# 
# Kryptering
# Kryptering er den mest komplekse datamaskeringsalgoritmen. Brukere kan bare få tilgang til data hvis de har dekrypteringsnøkkelen
# 
# <img src="https://research.aimultiple.com/wp-content/uploads/2020/07/Encryption-data-masking.png" alt="alternatetext">
# 
# Karakterkryptering
# Denne metoden innebærer å omorganisere rekkefølgen av tegn tilfeldig. Denne prosessen er irreversibel slik at de originale dataene ikke kan hentes fra de krypterte dataene.
# 
# Egnet for å dele data med uautoriserte brukere
# Nuller ut eller sletting
# Å erstatte sensitive data med nullverdi er også en tilnærming bedrifter kan foretrekke i deres datamaskeringsarbeid. Selv om det reduserer nøyaktigheten av testresultater som for det meste opprettholdes i andre tilnærminger, er det en enklere tilnærming når virksomheten ikke maskerer på grunn av modellvalideringsformål.
# 
# Maskering ut
# I maskeringsmetoden er bare en del av de originale dataene maskert. Det ligner på nulling ut siden det ikke er effektivt i testmiljøet. For eksempel, i netthandel, vises kun de siste 4 sifrene i kredittkortnummeret til kundene for å forhindre svindel.
# 
# <img src="https://research.aimultiple.com/wp-content/webp-express/webp-images/uploads/2020/07/data-masking.png.webp" alt="alternatetext">
# 
# 
# :::{figure-md} markdown-fig
# <img src="../images/sVSm.png" alt="Synthetic VS Masking" class="bg-primary mb-1" width="200px">
# 
# This is a caption in **Markdown**!
# :::
# 
# 
# --- 
# 
# <img src="https://research.aimultiple.com/wp-content/uploads/2020/07/Encryption-data-masking.png" alt="alternatetext">
# 
# Personvern blir stadig viktigere i dagens samfunn, og med GDPR har betydningen blitt enda større. Dette har ført til et økt behov for generering av syntetisk data for bruk i testing av nye løsninger. Men hva innebærer det egentlig å generere representativ syntetisk data som testere kan bruke, og som er i henhold til personlovgivningen? Kom og hør på vår lyntale om hvordan vi løste denne problemstillingen i  
# Å jobbe med data er vanskelig. Rådata byr vanligvis på flere utfordringer som må løses før du faktisk kan jobbe produktivt med dem. Noen ganger har du ikke nok data eller dataene har hull som må fylles. I mange tilfeller er det dyrt eller vanskelig å skaffe data på grunn av ytre forhold. I tillegg påvirker personvernbestemmelser måtene du kan bruke eller distribuere et datasett på. Av alle disse grunnene er bruk av syntetiske data et godt alternativ, siden det kan oppfylle de samme behovene med liten innsats.
# 
# Hva er syntetiske data?
# I henhold til definisjonen satt av Storbritannias Office for National Statistics (ONS):
# 
# "Syntetiske data er mikrodataposter opprettet for å forbedre dataverktøyet og samtidig forhindre avsløring av konfidensiell respondentinformasjon. Syntetiske data lages ved å statistisk modellere originaldata, og deretter bruke disse modellene til å generere nye dataverdier som reproduserer de originale dataenes statistiske egenskaper. Brukere er ikke i stand til å identifisere informasjonen til enhetene som ga de originale dataene."
# 
# ```{admonition} Definition 
# "Syntetiske data er mikrodataposter opprettet for å forbedre dataverktøyet og samtidig forhindre avsløring av konfidensiell respondentinformasjon. Syntetiske data lages ved å statistisk modellere originaldata og deretter bruke disse modellene til å generere nye dataverdier som reproduserer de originale dataenes statistiske egenskaper. Brukere er ikke i stand til å identifisere informasjonen til enhetene som ga de originale dataene."
# ```
# 
# Således har syntetiske data følgende tre viktige egenskaper:
# 
# * Syntetiske data lages fra en statistisk modell.
# * De statistiske egenskapene til syntetiske data bør være lik de originale dataene.
# * Syntetiske data skal anonymiseres.
# 
# 
# ONS-metodikken gir også en skala for å evaluere modenheten til et syntetisk datasett. Denne skalaen vurderer hvor mye de syntetiske dataene ligner de originale dataene, formålet og risikoen for avsløring. Metodikken inkluderer:
# 
# - Syntetisk strukturell: bevarer strukturen til de originale dataene, noe som er nyttig for å teste kode.
# - Syntetisk gyldig: bevarer ikke bare strukturen, men returnerer også verdier som er plausible i konteksten til datasettet. Du bør introdusere manglende verdikoder, feil og inkonsekvenser for å replikere de originale dataene.
# - Syntetisk utvidet plausibel: replikerer distribusjonene til hvert datautvalg der det er mulig uten å ta hensyn til forholdet mellom forskjellige kolonner (univariat).
# - Syntetisk utvidet multivariat plausibel: replikerer relasjoner på høyt nivå med plausible fordelinger (multivariat).
# - Syntetisk utvidet multivariat detaljert: replikerer detaljerte forhold. For denne må du utføre evaluering av informasjonskontroll fra sak til sak.
# - Syntetisk forsterket replika: gir nærmest mulig replikering. Det er avgjørende å utføre evaluering av avsløringskontroll fra sak til sak.
# 
# Hvert av de følgende bibliotekene bruker forskjellige tilnærminger til å generere syntetiske data. Noen fokuserer på å gi kun de syntetiske dataene i seg selv, men andre gir et komplett sett med verktøy som tar sikte på å oppnå den syntetisk utvidede replikaen beskrevet ovenfor.
# 
# ````{note}
# The next info should be nested
# ```{warning}
# Here's my warning
# ```
# ````
# 
# Således har syntetiske data tre viktige egenskaper:
# 
# * Syntetiske data lages fra en statistisk modell.
# * De statistiske egenskapene til syntetiske data bør være lik de originale dataene.
# * Syntetiske data skal anonymiseres.
# 
# ````{note}
# The warning block will be properly-parsed
# 
#    ```{warning}
#    Here's my warning
#    ```
# 
# But the next block will be parsed as raw text
# 
#     ```{warning}
#     Here's my raw text warning that isn't parsed...
#     ```
# ````
# 
# ```{admonition} My markdown link
# Here is [markdown link syntax](https://jupyter.org)
# ```
# 
# ```{admonition} My markdown link
# Here is [markdown link syntax](https://jupyter.org)
# ```
# 
# ```{math} e^{i\pi} + 1 = 0
# ---
# label: euler
# ---
# ```
# 
# Euler's identity, equation {math:numref}`euler`, was elected one of the
# most beautiful mathematical formulas.
# 
# 
# ONS-metodikken gir også en skala for å evaluere modenheten til et syntetisk datasett. Denne skalaen vurderer hvor mye de syntetiske dataene ligner de originale dataene, formålet og risikoen for avsløring. Metodikken inkluderer:
# 
# Syntetisk strukturell: bevarer strukturen til de originale dataene, noe som er nyttig for å teste kode.
# Syntetisk gyldig: bevarer ikke bare strukturen, men returnerer også verdier som er plausible i konteksten til datasettet. Du bør introdusere manglende verdikoder, feil og inkonsekvenser for å replikere de originale dataene.
# Syntetisk utvidet plausibel: replikerer distribusjonene til hvert datautvalg der det er mulig uten å ta hensyn til forholdet mellom forskjellige kolonner (univariat).
# Syntetisk utvidet multivariat plausibel: replikerer relasjoner på høyt nivå med plausible fordelinger (multivariat).
# Syntetisk utvidet multivariat detaljert: replikerer detaljerte forhold. For denne må du utføre evaluering av informasjonskontroll fra sak til sak.
# Syntetisk forsterket replika: gir nærmest mulig replikering. Det er avgjørende å utføre evaluering av avsløringskontroll fra sak til sak.
# Hvert av de følgende bibliotekene bruker forskjellige tilnærminger til å generere syntetiske data. Noen fokuserer på å gi kun de syntetiske dataene i seg selv, men andre gir et komplett sett med verktøy som tar sikte på å oppnå den syntetisk utvidede replikaen beskrevet ovenfor.
# 
# 
# [Synthetic](https://mostly.ai/blog/synthetic-data-generator-for-healthy-test-data/)
# **Synthetic test data**  is generated by AI, that is trained on real data. It is structurally representative, referential integer data with support for relational structures. AI-generated synthetic data is not mock data or fake data. It is as much a representation of the behavior of your customers as production data. It’s not generated manually, but by a powerful AI engine that is capable of learning all the qualities of the dataset it is trained on, providing 100% test coverage. A good quality synthetic data generator can automate test data generation with high efficiency and without privacy concerns. Customer data should always be used in its synthetic form to protect privacy and to retain business rules embedded in the data. For example, mobile banking apps should be tested with synthetic transaction data, that is based on real customer transactions. 
# 
# TL;DR
# Synthetic data generation methods changed significantly with the advance of AI
# AI-generated, sample-based synthetic data is an entirely different beast than random or mock data
# Types of AI-generated synthetic data include synthetic images, synthetic text, synthetic geolocation data, categorical, numerical and time-series data.
# Stochastic processes are still useful if you care about data structure but not content
# Rule-based systems can be used for simple use cases with low, fixed requirements toward complexity
# Use deep generative models to automatically retain structure as well as information of data at scale to unlock private data and reduce model-to-market time
# What the most common synthetic data types and their most common use cases are.
# An overview of data generation methods
# Not all synthetic dataset is created equal and in particular, synthetic data generation today is very different from what it was 5 years ago. Let’s take a look at different methods of synthetic data generation from the most rudimental forms to the state-of-the-art methods to see how far the technology has advanced! In this post we will distinguish between three major methods:
# 
# The stochastic process: random data is generated, only mimicking the structure of real data.
# Rule-based data generation: mock data is generated following specific rules defined by humans.
# Deep generative models: rich and realistic synthetic data is generated by a machine learning model trained on real data, replicating its structure and the information it contains.
# 
# # Definitions
# 
# 
# SMOTE (Synthetic Minority Oversampling Technique) to deal with imbalanced classes in a dataset.
# 
# Another well-known technique is called SMOTE, which involves data augmentation (i.e., synthesizing new data samples) well before you use a clas- sification algorithm. SMOTE was initially developed by means of the kNN algorithm (other options are available), and it can be an effective technique for handling imbalanced classes.
# Yet another option to consider is the Python package imbalanced-learn in the scikit-learn-contrib project. This project provides various re-sampling techniques for datasets that exhibit class imbalance. More details are available online:
# https://github.com/scikit-learn-contrib/imbalanced-learn.
# https://www.datprof.com/solutions/synthetic-test-data-generation/
# 
# 
# https://mostly.ai/wp-content/uploads/2021/09/MOSTLY-AI_comparison_of_synthetic_data_types_2-1-1024x724.png
# 
# 
# WHAT IS SMOTE?
# SMOTE is a technique for synthesizing new samples for a dataset. This tech- nique is based on linear interpolation:
# Step 1: Select samples that are close in the feature space.
# Step 2: Draw a line between the samples in the feature space.
# Step 3: Draw a new sample at a point along that line.
# A more detailed explanation of the SMOTE algorithm is as follows:
# Select a random sample “a” from the minority class.
# Find k nearest neighbors for that example.
# Select a random neighbor “b” from the nearest neighbors.
# Create a line “L” that connects “a” and “b.”
# Randomly select one or more points “c” on line L.
# If need be, you can repeat this process for the other (k-1) nearest neigh- bors to distribute the synthetic values more evenly among the nearest neighbors.
# SMOTE Extensions
# The initial SMOTE algorithm is based on the kNN classification algorithm, which has been extended in various ways, such as replacing kNN with SVM. A list of SMOTE extensions is shown as follows:
# selective synthetic sample generation
# Borderline-SMOTE (kNN)
# Borderline-SMOTE (SVM)
# Adaptive Synthetic Sampling (ADASYN)
