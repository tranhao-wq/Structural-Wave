import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  LabelList,
  ResponsiveContainer
} from "recharts";

const data = [
  {
    wave: "K1",
    phaseA: 27,
    phaseB: 30,
    juglarA: 3,
    juglarB: 3,
    tech: "Cách mạng công nghiệp I"
  },
  {
    wave: "K2",
    phaseA: 26,
    phaseB: 27,
    juglarA: 3,
    juglarB: 3,
    tech: "Đường sắt, thép"
  },
  {
    wave: "K3",
    phaseA: 38,
    phaseB: 20,
    juglarA: 4,
    juglarB: 2,
    tech: "Ô tô, điện, hóa học"
  },
  {
    wave: "K4",
    phaseA: 26,
    phaseB: 16,
    juglarA: 3,
    juglarB: 2,
    tech: "Sản xuất hàng loạt, dầu mỏ"
  },
  {
    wave: "K5",
    phaseA: 18,
    phaseB: 6,
    juglarA: 2,
    juglarB: 1,
    tech: "CNTT, AI, Big Data"
  }
];

export default function InteractiveKChart() {
  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4 text-center">
        Biểu đồ Tương tác Sóng Kondratieff K1–K5
      </h2>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} margin={{ top: 20, right: 20, left: 0, bottom: 50 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="wave" />
          <YAxis label={{ value: 'Số năm', angle: -90, position: 'insideLeft' }} />
          <Tooltip formatter={(value, name) => [`${value} năm`, name === 'phaseA' ? 'Pha A' : 'Pha B']} />
          <Legend />

          <Bar dataKey="phaseA" fill="#ffffff" stroke="#000" name="Pha A (Tăng trưởng)">
            <LabelList dataKey="juglarA" position="top" formatter={(val) => `J×${val}`} fill="#0074D9" />
          </Bar>

          <Bar dataKey="phaseB" fill="#000000" name="Pha B (Suy thoái)">
            <LabelList dataKey="juglarB" position="top" formatter={(val) => `J×${val}`} fill="#7FDBFF" />
          </Bar>
        </BarChart>
      </ResponsiveContainer>

      <div className="mt-6">
        {data.map((d) => (
          <div key={d.wave} className="text-center mb-2">
            <strong>{d.wave}</strong>: <span className="text-green-700">{d.tech}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
