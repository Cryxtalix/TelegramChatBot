{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    ollama
  ] ++ 
  (with pkgs.python311Packages; [
    # pip packages
    pip
    python-dotenv
    telethon
    cryptg
    requests
  ]);
  shellHook = ''
    echo "Started python Telethon development environment..."
  '';
}
