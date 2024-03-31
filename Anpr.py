{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNzF35ZGyoQN2XnXh68Hnlc",
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
        "<a href=\"https://colab.research.google.com/github/jasmine400/automatic-number-plate-recognetion/blob/main/Anpr.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5dnkG2V4-_9n",
        "outputId": "1bf9c4b4-d0e8-4639-a6fa-5d0f7384ec9b"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/drive/My\\ Drive/c"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bs7CZrPuLdTm",
        "outputId": "0fed86f4-78a3-461a-9e03-ebff9b000e52"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/My Drive/c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get install git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YHRwrvKKLkfQ",
        "outputId": "2287cc37-4e9e-40a3-8f5b-cfd0265f5fd6"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "git is already the newest version (1:2.34.1-1ubuntu1.10).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 45 not upgraded.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git config --global user.email \"yasaman99teymouri@gmail.com\"\n",
        "!git config --global user.name \"jasmine400\""
      ],
      "metadata": {
        "id": "QyGs_GcxLo3Z"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/username/automatic-number-plate-recognetion.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i_HBMdQML37w",
        "outputId": "6bfb0463-63b8-4079-d28c-67d291739623"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'automatic-number-plate-recognetion'...\n",
            "fatal: could not read Username for 'https://github.com': No such device or address\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/jasmine400/automatic-number-plate-recognetion.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5ZsqMAUN_hS9",
        "outputId": "8c85727a-fa63-440f-9902-7fb3726fe608"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'automatic-number-plate-recognetion'...\n",
            "remote: Enumerating objects: 3, done.\u001b[K\n",
            "remote: Counting objects: 100% (3/3), done.\u001b[K\n",
            "remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Receiving objects: 100% (3/3), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!cp Anpr.py /content/drive/My\\ Drive/c/automatic-number-plate-recognetion"
      ],
      "metadata": {
        "id": "ca-gB-8aMVDk"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/drive/My\\ Drive/c/automatic-number-plate-recognetion"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rl-TEAGHMnTL",
        "outputId": "18637917-3c0d-4677-9e78-30d10e5a7ac5"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/My Drive/c/automatic-number-plate-recognetion\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PRMyfo7lMzIT",
        "outputId": "f93e0f31-cc73-468e-99d5-ff1741cc27b4"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Anpr.py  README.md\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git add Anpr.py"
      ],
      "metadata": {
        "id": "sx_Ww5kPMuK0"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git commit -m \"Add Anpr.py file\""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kuODkXT_M-g8",
        "outputId": "cfb19138-f0b1-4596-f795-40c156778977"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[main 723d435] Add Anpr.py file\n",
            " 1 file changed, 156 insertions(+)\n",
            " create mode 100644 Anpr.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git push -u origin main"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rGAsL1pxNFRq",
        "outputId": "ef6e1753-b60d-4bf1-c5bd-882258298748"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: could not read Username for 'https://github.com': No such device or address\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git credential fill"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GVhO2p5XOXuC",
        "outputId": "9f0c0f30-b1cd-484b-fb81-e9a2e1f843bb"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "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\n",
            "warning: invalid credential line: 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\n",
            "fatal: unable to read credential from stdin\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git config --global user.name \"jasmine400\"\n",
        "!git config --global user.email \"yasaman99teymouri@gmail.com\""
      ],
      "metadata": {
        "id": "jiDlOK7sOIYH"
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%cd automatic-number-plate-recognetion"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KzaGfEkNAbj4",
        "outputId": "9e93a408-7754-46fa-9cea-2affb1ec4a42"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/c/automatic-number-plate-recognetion\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git add Anpr.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gioLBX-h_z6W",
        "outputId": "c4bb3052-e1ff-4e4e-e08e-dae0e57539e4"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: pathspec 'Anpr.py' did not match any files\n"
          ]
        }
      ]
    }
  ]
}