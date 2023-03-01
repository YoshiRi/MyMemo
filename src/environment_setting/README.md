PCの諸々のSettingをメモする


# Fish

```
# fish-shell
sudo apt-get update
sudo apt-get install fish

# dependent libraries
sudo apt-get install fzf fd-find jq
ln -s $(which fdfind) ~/.local/bin/fd

# Fisher
fish -c "curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher"

# recommended fish plugins
fish -c "fisher install rafaelrinaldi/pure oh-my-fish/plugin-pbcopy edc/bass jethrokuan/fzf decors/fish-ghq"

# kenji-miyake's fish plugins
fish -c "fisher install kenji-miyake/reload.fish kenji-miyake/vcd.fish kenji-miyake/auto-source-setup-bash.fish kenji-miyake/colcon-clean.fish kenji-miyake/colcon-abbr.fish"

# argcomplete
pip3 install --user argcomplete
echo 'register-python-argcomplete --shell fish ros2 | source' >> ~/.config/fish/config.fish
```

最新版は[Miyake氏のrepo](https://github.com/kenji-miyake/dotfiles)にて。


# tmux

.tmux.confをメモ

# Grid workspace

下準備1

```
sudo apt-get install chrome-gnome-shell
```

下準備2（拡張機能インストール）

https://extensions.gnome.org/extension/1485/workspace-matrix/

