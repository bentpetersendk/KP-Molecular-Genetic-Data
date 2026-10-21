---
title: Resources
---

# Resources

## General

- [Galaxy Europe](https://usegalaxy.eu)
- [A short introduction to Galaxy](https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-short/tutorial.html)
- [Galaxy Help forum](https://help.galaxyproject.org/)

## The Unix command line

### Documentation

- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/html_node/index.html): `ls`, `cp`, `mv`, `rm`, `head`, `tail`, `wc`, `cut`, `paste`, `sort`, `uniq` and more
- [GNU grep manual](https://www.gnu.org/software/grep/manual/grep.html): options and regular expressions

### Further practice

- [CLI basics](https://training.galaxyproject.org/training-material/topics/data-science/tutorials/cli-basics/tutorial.html) (Galaxy Training Network): the command line in the same kind of Galaxy terminal
- [The Unix Shell](https://swcarpentry.github.io/shell-novice/) (Software Carpentry): a longer self-study lesson

### Data sources

- [UniProt](https://www.uniprot.org): the protein database the practical's data come from ([licence: CC BY 4.0](https://www.uniprot.org/help/license); [FASTA header format](https://www.uniprot.org/help/fasta-headers))

## NGS preprocessing and quality control

### Tools

| Tool | Documentation |
|---|---|
| FastQC | [Project page](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) · [Help: what each report module means](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/) |
| Cutadapt | [User guide](https://cutadapt.readthedocs.io/en/stable/guide.html) |
| Trimmomatic | [Project page](http://www.usadellab.org/cms/?page=trimmomatic) · [Source and manual](https://github.com/usadellab/Trimmomatic) |

### Further reading

- [Quality control tutorial](https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/quality-control/tutorial.html) (Galaxy Training Network): further reading on the topics of this practical

### Data sources

- [1000 Genomes Project, sample HG00418](https://www.internationalgenome.org/data-portal/sample/HG00418): the human sample used in this practical

## Read mapping and variant calling

### Tools

| Tool | Documentation |
|---|---|
| BWA-MEM | [Manual](https://bio-bwa.sourceforge.net/bwa.shtml) · [Source](https://github.com/lh3/bwa) |
| SAMtools and BCFtools | [Manual pages](https://www.htslib.org/doc/) |
| bedtools | [Documentation](https://bedtools.readthedocs.io/) |
| Snippy | [Source and manual](https://github.com/tseemann/snippy) |
| Picard MarkDuplicates | [Picard documentation](https://broadinstitute.github.io/picard/) |
| JBrowse 2 | [Documentation](https://jbrowse.org/jb2/docs/) |

### File formats

- [SAM/BAM format specification](https://samtools.github.io/hts-specs/SAMv1.pdf)
- [Explain SAM flags](https://broadinstitute.github.io/picard/explain-flags.html): decode a FLAG value
- [VCF format specification](https://samtools.github.io/hts-specs/VCFv4.3.pdf)

### Further reading

- [Mapping](https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/mapping/tutorial.html) (Galaxy Training Network)
- [Microbial variant calling](https://training.galaxyproject.org/training-material/topics/variant-analysis/tutorials/microbial-variants/tutorial.html) (Galaxy Training Network): Snippy on a bacterial genome
- Li H, Durbin R (2009) Fast and accurate short read alignment with Burrows–Wheeler transform. *Bioinformatics* 25:1754–1760. [doi:10.1093/bioinformatics/btp324](https://doi.org/10.1093/bioinformatics/btp324)
- Danecek P, et al. (2021) Twelve years of SAMtools and BCFtools. *GigaScience* 10:giab008. [doi:10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008)
- Andersen SB, Marvig RL, Molin S, Krogh Johansen H, Griffin AS (2015) Long-term social dynamics drive loss of function in pathogenic bacteria. *PNAS* 112:10756–10761. [doi:10.1073/pnas.1508324112](https://doi.org/10.1073/pnas.1508324112)

### Data sources

- [ENA run ERR706017](https://www.ebi.ac.uk/ena/browser/view/ERR706017): the *P. aeruginosa* reads (a cystic fibrosis isolate of the Danish lineage DK01)
- [NCBI RefSeq NC_002516.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_002516.2): the PAO1 reference genome (Stover CK, et al. (2000) *Nature* 406:959–964, [doi:10.1038/35023079](https://doi.org/10.1038/35023079))
- [Pseudomonas Genome Database](https://www.pseudomonas.com): gene information for PAO1 locus tags
- [1000 Genomes Project, sample HG00418](https://www.internationalgenome.org/data-portal/sample/HG00418) and [ENA run ERR1044272](https://www.ebi.ac.uk/ena/browser/view/ERR1044272): the human reads

<!-- TODO(instructors): add reading lists, papers and other course resources here: course-wide items under General, practical-specific items under the practical's heading. -->
