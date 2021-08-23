{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Task1,2.py",
      "provenance": [],
      "authorship_tag": "ABX9TyOycIC2reFRkncD7UMPFi1O",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/janubr/shadow_wales/blob/main/Task1%2C2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mFtKzxGP9bGO"
      },
      "source": [
        "### Fibonnaci using sequence"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5M7R5v4_upJZ",
        "outputId": "c62b37a0-e591-4ecf-c6da-8ec9a5ffdf37"
      },
      "source": [
        "def fib_rec(n):\n",
        "     if n == 1:\n",
        "         return [0]\n",
        "     elif n == 2:\n",
        "         return [0,1]\n",
        "     else:\n",
        "      x= fib_rec(n-1)\n",
        "      x.append(sum(x[1-1:-1]))\n",
        "      return x\n",
        "x=fib_rec(15)\n",
        "print(x) "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i10u6QpB9M2u"
      },
      "source": [
        "### Fibonacci using recursion"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zMaIXaxK718S",
        "outputId": "3b59e4fa-2e47-4ea0-fa9d-1b1443378073"
      },
      "source": [
        "def fibonacci(n):\n",
        "    if n<0:\n",
        "       print(\"Incorrect input\")\n",
        "    # first fibonacci number is 0\n",
        "    elif n==0:\n",
        "       return 0\n",
        "    # second fibonacci number is 1\n",
        "    elif n ==1:\n",
        "        return 1\n",
        "    else:\n",
        "        return fibonacci(n-1)+fibonacci(n-2)\n",
        "\n",
        "print(fibonacci(12))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "144\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2mrsBdYB7U1G"
      },
      "source": [
        "### Positive numbers in range"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YGjRvjpb9utC",
        "outputId": "4bb73b77-0d8f-44e6-9961-4e10b36319b4"
      },
      "source": [
        "list1 = [12, -7, 5, 64, -14]\n",
        "for num in list1:\n",
        "\n",
        "  if num >= 0:\n",
        "\n",
        "    print(num,end = \" \")"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "12 5 64 "
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UcxvQnlm6JoV",
        "outputId": "c8b54ae8-7c93-41eb-9c85-158d3bb00185"
      },
      "source": [
        "list2 = [12, 14, -95, 3]\n",
        "for num in list2:\n",
        "    \n",
        "    if num >= 0:\n",
        "\n",
        "      print(num, end = \" \")"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "12 14 3 "
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}