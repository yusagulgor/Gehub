class Gethub:
    # ffpy da cargo run

    """
    # Usage
    Please click on the class and read the doc.

    !!! # Kullanmadan önce zaten github hesabında repo oluşturulmalı . 

    !!! # Proje path kısmına çift slash koymayı unutma.

    proje_path must be like this: "x:\\examples\\..." The important thing here is to double \ backslashes.

    Args:
        proje_path (str): Proje dizin yolu.
        repo_url (str): GitHub repository URL'si.
        branch_name (str): Git dalı adı.
        commit_message (str): Commit mesajı..

    """

    def __init__(self, proje_path: str, repo_url: str, your_branchName: str, commitMessage: str) -> None:
        self.pPath = proje_path

        self.rPath = repo_url
        self.y_bN = your_branchName

        # print(f"dizin : {os.getcwd()}")  

        if commitMessage.__len__() > 18:
            raise ValueError("commit message cant be 16 and more.")

        self.cm = commitMessage

    def run(self):
        import ctypes
        lib = ctypes.CDLL("src\\modules\\fgit.dll")
        lib.push_to_github.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        lib.push_to_github.restype = ctypes.c_char_p

        encoded_path = self.pPath.encode("utf-8")
        encoded_url = self.rPath.encode("utf-8")
        encoded_branch = self.y_bN.encode("utf-8")
        encoded_message = self.cm.encode("utf-8")

        result = lib.push_to_github(encoded_path, encoded_url, encoded_branch, encoded_message)
        return ctypes.string_at(result).decode("utf-8")