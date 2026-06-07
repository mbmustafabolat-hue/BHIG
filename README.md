# B-HİG — Bolat Hâl-İlişki Geometrodinamiği

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20582146.svg)](https://doi.org/10.5281/zenodo.20582146)

> Scientific status: This repository presents B-HİG as a theoretical research framework and computational model candidate, not as an established physical theory.

> Bilimsel statü: Bu depo, B-HİG’i kanıtlanmış bir fizik teorisi olarak değil; teorik araştırma çerçevesi ve hesaplanabilir model adayı olarak sunar.

# Bolat Hâl-İlişki Geometrodinamiği (B-HİG)

**B-HİG**, İlişkisel Oluş Yorumu üzerine kurulu bir teori adayıdır. Temel fikir: fiziksel evren, kararlı hâller-arası ilişki matrisi `W*`nin iyi iç saat altında görünen projeksiyonudur.

```text
E_phys = P_tau(W*)
W* = argmin_{W in Fix(R)} E_BHIG[W]
```

## Statü

Bu depo, kanıtlanmış nihai fizik teorisi değil; B-HİG araştırma programı için açık, tartışılabilir ve çalıştırılabilir bir başlangıç paketidir.

- Test edilebilir fizik iddiaları `docs/05_Test_Edilebilir_Fizik.md` altında tutulur.
- Bilinç, benlik, reenkarnasyon ve metafizik yorumlar `docs/06_Bilinc_ve_Metafizik.md` altında, bilimsel iddia değil felsefi uzantı olarak işaretlenir.
- Spekülatif başlıklar `docs/07_Spekulatif_Yorumlar.md` altında ayrılır.

## Kurulum

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python examples/run_demo.py
```

## Depo yapısı

```text
README.md
LICENSE
CITATION.cff
requirements.txt
docs/
src/
examples/
data/
results/
figures/
```

## Ana belgeler

- `docs/final/BHIG_Nihai_Ana_Dokuman_v1.pdf`
- `docs/final/BHIG_Akademik_Makale_TR_v1.pdf`
- `src/bhig_wstar_model.py`

## Atıf
Bolat, M. (2026). Bolat Hâl-İlişki Geometrodinamiği (B-HİG): İlişkisel Uzay-Zaman İçin Teorik ve Hesaplanabilir Araştırma Çerçevesi (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20582146

@misc{bolat2026bhig,
  author       = {Bolat, Mustafa},
  title        = {Bolat Hâl-İlişki Geometrodinamiği (B-HİG): İlişkisel Uzay-Zaman İçin Teorik ve Hesaplanabilir Araştırma Çerçevesi},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.20582146},
  url          = {https://doi.org/10.5281/zenodo.20582146}
}

Bu çalışma için `CITATION.cff` dosyasını kullanabilirsiniz.
