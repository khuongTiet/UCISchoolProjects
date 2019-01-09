#include <iostream>
using namespace std;

template <typename T> class Vector
{
private:
  int sz;
  T *buf;
public:
  Vector(int n) {
    this->sz = n;
    this->buf = new T[n];
  }

  Vector<T>(initializer_list<T> L) {
    this->sz = L.size();
    this->buf = new T[this->sz];
    int temp = 0;
    for (T i : L) {
      this->buf[temp] = i;
      temp++;
    }
  }

  ~Vector<T>() {
    delete[] this->buf;
  }

  Vector(const Vector& v) {
    this->sz = v.sz;
    this->buf = new T[this->sz];
    for (int i = 0; i < this->sz; i++) {
      this->buf[i] = v.buf[i];
    }
  }

  int size() {
    return this->sz;
  }

  T& operator[](const int i) {
    if (i > this->sz) {
      cout << "ERROR: Out of Bounds" << endl;
    }
    else{
      return this->buf[i];
    }
  }

  T operator*(const Vector& v) const {
    if (this->sz != v.sz) {
      cout << "ERROR: Different sizes, returning smaller vector" << endl;
    }
    T temp = 0;
    int limit = min(this->sz, v.sz);
    for (int i = 0; i < limit; i++) {
      temp += this->buf[i] * v.buf[i];
    }
    return temp;
  }

  Vector operator+(const Vector& v) const {
    if (this->sz != v.sz) {
      cout << "ERROR: Different sizes, returning smaller Vector" << endl;
    }
    int size = min(this->sz, v.sz);
    Vector<T> temp(size);
    for (int i = 0; i < size; i++) {
      temp.buf[i] = this->buf[i] + v.buf[i];
    }
    return temp;
  }

  const Vector &operator= (const Vector &v) const {
    for (int i = 0; i < v.sz; i++) {
      this->buf[i] = v.buf[i];
    }
  }

  bool operator == ( const Vector& v) const {
    if (this->sz != v.sz) {
      return false;
    }
    else {
      for (int i = 0; i < this->sz; i++) {
        if (this->buf[i] != v.buf[i]) {
          return false;
        }
      }
      return true;
    }
  }

  bool operator != (const Vector& v) const {
    if (this->sz != v.sz) {
      return true;
    }
    else {
      for (int i = 0; i < this->sz; i++) {
        if (this->buf[i] != v.buf[i]) {
          return true;
        }
      }
      return false;
    }
  }

  friend Vector operator*(const int n, const Vector& v) {
    Vector<T> temp(v.sz);
    for (int i = 0; i < v.sz; i++) {
      temp.buf[i] = v.buf[i] * n;
    }
    return temp;
  }

  friend Vector operator+(const int n, const Vector& v) {
    Vector<T> temp(v.sz);
    for (int i = 0; i < v.sz; i++) {
      temp.buf[i] = v.buf[i] + n;
    }
    return temp;
  }

  friend ostream& operator<<(ostream& o, const Vector& v) {
    for (int i = 0; i < v.sz; i++) {
      o << v.buf[i] << " ";
    }
    return o;
  }
};

int main() {
  Vector<int> intVec{1,3,5,7,9};
  Vector<int> intVec2{2,4,6,8,10};
	Vector<double> doubleVec{1.5,2.5,3.5,4.5};
  cout << intVec[1] << endl;
  cout << doubleVec[2] << endl;
	Vector<int> iv(intVec);
  cout << iv << endl;
	Vector<double> dv(doubleVec);
  cout << dv << endl;
  Vector<int> v1(10);
  cout << v1.size() << endl;
  Vector<double> d1(5);
  cout << d1.size() << endl;
  cout << intVec[1] << endl;
  cout << intVec[10] << endl;
  cout << intVec * intVec2 << endl;
  Vector<int> intVec3 = intVec + intVec2;
  intVec = intVec2;
  if (intVec == intVec2)
    cout << "EQUALS" << endl;
  if (intVec != intVec2)
    cout << "NOT EQUALS" << endl;
  Vector<int> intVec4 = 2 * intVec;
  cout << intVec4 << endl;
  Vector<int> intVec5 = 4 + intVec3;
  cout << intVec5 << endl;
  Vector<int> intVec6 = {1, 2};
  Vector<double> d2{2.0, 1.0, 3.0};
  Vector<double> d3{3.0, 4.0, 5.0};
  cout << 2 * d2 << endl;
  cout << d2 + doubleVec << endl;
  cout << intVec6 * intVec << endl;
  return 0;
}
