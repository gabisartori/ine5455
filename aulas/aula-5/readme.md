# Apresentação

## Mutantes Sobreviventes
move_tile:
- Mutante 8: conteudo.puzzle_game.xǁPuzzleGameǁmove_tile__mutmut_3
- Mutante 9: conteudo.puzzle_game.xǁPuzzleGameǁmove_tile__mutmut_20

get_tile:
- Mutante 1: conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_2
- Mutante 2: conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_3
- Mutante 3: conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_4
- Mutante 4: conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_6
- Mutante 5: conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_7
- Mutante 6: conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_9
- Mutante 7: conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_10

## Mutantes a serem apresentados
| mutante | teste respectivo|
| - | - |
| move_tile__mutmut_3 | test_movimento_com_sucesso_verifica_peça_movida |
| move_tile__mutmut_20 | test_verifica_tile_apos_movimento |
| get_tile__mutmut_2 | test_get_tile_outside_board_with_negative_line_and_valid_column |
| get_tile__mutmut_3 | test_get_tile_at_line_greater_than_0_but_invalid_column |
| get_tile__mutmut_10 | test_get_valid_tile_at_line_of_empty_position |


# Execução
O script `run.sh` executa todos os passos a seguir automaticamente. Esta seção serve para que o passo-a-passo possa ser apresentado naturalmente

## Apenas com testes antigos
Apague a pasta `mutants` para garantir que a cache dos testes não utilize os novos testes prematuramente

```bash
PYTHONPATH=conteudo:tests mutmut run
mutmut results | grep -E "(move_tile|get_tile)__mutmut_[0-9]+"
```

O comando grep fará o trabalho de filtrar os mutantes que não importam para a atividade, exibindo apenas os mutantes a serem mortos.

## Com testes novos para matar os mutantes selecionados
Após renomear `tests/test_new.py.bak` para `tests/test_new.py`, execute

```bash
PYTHONPATH=conteudo:tests mutmut run
mutmut results | grep -E "(move_tile|get_tile)__mutmut_[0-9]+"
```

Agora, após a filtragem dos resultados, nenhum dos mutantes de interesse aparecem como sobreviventes.

Note que `mutmut results` ainda retornará diversos outros mutantes, para partes do código que não são o alvo da atividade.
