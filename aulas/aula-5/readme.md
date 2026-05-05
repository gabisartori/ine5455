# Apresentação para a professora

## Mutantes Sobreviventes
move_tile:
- conteudo.puzzle_game.xǁPuzzleGameǁmove_tile__mutmut_3
- conteudo.puzzle_game.xǁPuzzleGameǁmove_tile__mutmut_20

get_tile:
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_2
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_3
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_4
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_6
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_7
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_9
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_10

## Mutantes a serem apresentados
- conteudo.puzzle_game.xǁPuzzleGameǁmove_tile__mutmut_3
- conteudo.puzzle_game.xǁPuzzleGameǁmove_tile__mutmut_20
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_2
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_3
- conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_10


# Execução
## Apenas com testes antigos
Basta executar

```bash
PYTHONPATH=src:tests mutmut run
mutmut results
```

Note que o resultado contém os mutantes listados no começo do arquivo como sobreviventes

## Com testes novos para matar os mutantes selecionados
Após renomear `tests/test_new.py.bak` para `tests/test_new.py`, execute

```bash
PYTHONPATH=src:tests mutmut run
mutmut results
```

Note que os mutantes listados previamente não estão mais na lista de mutantes sobreviventes