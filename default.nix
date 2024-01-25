{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
  ] ++ 
  (with pkgs.python311Packages; [
    # pip packages
    pip
    python-dotenv
    telethon
    cryptg
    httpx
  ]);
  shellHook = ''
    echo "Started python Telethon development environment..."
  '';
}
