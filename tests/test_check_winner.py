import pytest
from models.board import Board

def test_column_win():
    #First Column Test
    first_column_win = Board()
    first_column_win.update_board(0, 0, "X")
    first_column_win.update_board(1, 0, "X")
    first_column_win.update_board(2, 0, "X")
    assert first_column_win.check_winner() == True

    #Second Column Test
    second_column_win = Board()
    second_column_win.update_board(0, 1, symbol="X")
    second_column_win.update_board(1, 1, symbol="X")
    second_column_win.update_board(2, 1, symbol="X")
    assert second_column_win.check_winner() == True

    #Third Column Test
    third_column_win = Board()
    third_column_win.update_board(0, 2, "X")
    third_column_win.update_board(1, 2, "X")
    third_column_win.update_board(2, 2, "X")
    assert third_column_win.check_winner() == True

def test_row_win():
    #First Row Test
    first_row_win = Board()
    first_row_win.update_board(0, 0, "X")
    first_row_win.update_board(0, 1, "X")
    first_row_win.update_board(0, 2, "X")
    assert first_row_win.check_winner() == True

    #Second Row Test
    second_row_win = Board()
    second_row_win.update_board(1, 0, "X")
    second_row_win.update_board(1, 1, "X")
    second_row_win.update_board(1, 2, "X")
    assert second_row_win.check_winner() == True

    #Third Row Test
    third_row_win = Board()
    third_row_win.update_board(2, 0, "X")
    third_row_win.update_board(2, 1, "X")
    third_row_win.update_board(2, 2, "X")
    assert third_row_win.check_winner() == True

def test_diagonal_win():
    #Down Right to Left
    diagonal_A_win = Board()
    diagonal_A_win.update_board(0, 2, "X")
    diagonal_A_win.update_board(1, 1, "X")
    diagonal_A_win.update_board(2, 0, "X")
    assert diagonal_A_win.check_winner() == True

    #Down Left to Right
    diagonal_B_win = Board()
    diagonal_B_win.update_board(0, 0, "X")
    diagonal_B_win.update_board(1, 1, "X")
    diagonal_B_win.update_board(2, 2, "X")
    assert diagonal_B_win.check_winner() == True